#define _GNU_SOURCE
#define BUF_SIZE 64 * 1024 * 1024

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <dirent.h>
#include <string.h>
#include <sys/file.h>
#include <fcntl.h>
#include <ctype.h>

char* select_disk() {
	DIR* dirptr = opendir("/dev/");
	if (dirptr==NULL) {
		perror("Failed to open dir");
		return NULL;
	}

	struct dirent *entry;
	char* result = (char*)calloc(512, sizeof(char));
	const char* sd_prefix = "sd";
	const char* xvd_prefix = "xvd";
	while(entry=readdir(dirptr)) {
		if(strncmp(sd_prefix, entry->d_name, 2)==0 || strncmp(xvd_prefix, entry->d_name, 3)==0)  {
			snprintf(result, 512*sizeof(char), "/dev/%s", entry->d_name);
			return result;
		}
	}

	free(result);
	return NULL;
}

void sub_process(const char* disk)
{
	int fd = open(disk, O_RDONLY|O_DIRECT|O_LARGEFILE, 0755);
	if (fd<0) {
		perror("failed to open disk");
		_exit(1);
	}

	unsigned char* buf;
	posix_memalign((void **)&buf, 512, BUF_SIZE);
	int read_bytes=0;
	while (read_bytes < 20 * BUF_SIZE)
	{
		int ret = read(fd, buf, BUF_SIZE);
		if (ret < 0)
		{
			perror("failed to read contents");
			close(fd);
			free(buf);
			_exit(1);
		}
		read_bytes += ret;
	}

	close(fd);
	free(buf);
	_exit(0);

}

int main(int argc, char **argv)
{
	int status = 0;
	int c = 0;
	char *disk = NULL;

	while ((c = getopt(argc, argv, "d:")) != -1)
	{
		switch (c)
		{
		case 'd':
			disk = optarg;
			break;
		case '?':
			printf("Illegal option: -%c\n", isprint(optopt) ? optopt : '#');
			_exit(1);
		default:
			_exit(1);
		}
	}

	if (disk == NULL)
	{
		disk = select_disk();
	}
	if (disk == NULL)
	{
		_exit(1);
	}

	printf("Reading data from disk %s\n", disk);

	for (;;) {
		for (int i = 0; i < 2; i++) {
			if(fork()== 0) {
				sub_process(disk);
			}
		}
		sleep(5);
	}

	while(wait(&status)>0);
	return 0;
}
