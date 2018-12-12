#define _GNU_SOURCE
#define BUF_SIZE 32 * 1024 * 1024

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <dirent.h>
#include <string.h>
#include <sys/file.h>
#include <fcntl.h>
#include <ctype.h>

char *select_disk()
{
	DIR *dirptr = opendir("/dev/");
	if (dirptr == NULL)
	{
		perror("Failed to open dir");
		return NULL;
	}

	struct dirent *entry;
	char *result = (char *)calloc(512, sizeof(char));
	const char *sd_prefix = "sd";
	const char *xvd_prefix = "xvd";
	while (entry = readdir(dirptr))
	{
		if (strncmp(sd_prefix, entry->d_name, 2) == 0 || strncmp(xvd_prefix, entry->d_name, 3) == 0)
		{
			snprintf(result, 512 * sizeof(char), "/dev/%s", entry->d_name);
			return result;
		}
	}

	free(result);
	return NULL;
}

long int get_value(char *str)
{
	char *endptr = NULL;
	long int value = strtol(str, &endptr, 10);
	if ((errno == ERANGE && (value == LONG_MAX || value == LONG_MIN)) || (errno != 0 && value == 0))
	{
		perror("strtol");
		return -1;
	}

	if (endptr == str)
	{
		perror("not number");
		return -1;
	}

	if (value <= 0)
	{
		perror("not positive number");
		return -1;
	}

	return value;
}

void app(const char *disk, long int buffer_size)
{
	int flags = O_RDONLY | O_LARGEFILE | O_DIRECT;
	int fd = open(disk, flags, 0755);
	if (fd < 0)
	{
		perror("failed to open disk");
		_exit(1);
	}

	unsigned char *buf;
	struct timeval start, end;
	posix_memalign((void **)&buf, 512, buffer_size);
	int read_bytes = 0;
	gettimeofday(&start, NULL);
	while (read_bytes < buffer_size)
	{
		int ret = read(fd, buf, buffer_size);
		if (ret < 0)
		{
			perror("failed to read contents");
			close(fd);
			free(buf);
			_exit(1);
		}
		read_bytes += ret;
	}

	gettimeofday(&end, NULL);
	double total_time = (end.tv_sec - start.tv_sec) + (end.tv_usec - start.tv_usec) / 1000000.0;
	printf("Time used: %f s to read %ld bytes\n", total_time, buffer_size);
	close(fd);
	free(buf);
}

int main(int argc, char **argv)
{
	int status = 0;
	int c = 0;
	char *disk = NULL;
	char *size = NULL;

	while ((c = getopt(argc, argv, "d:s:")) != -1)
	{
		switch (c)
		{
		case 'd':
			disk = optarg;
			break;
		case 's':
			size = optarg;
			break;
		case '?':
			printf("Illegal option: -%c\n", isprint(optopt) ? optopt : '#');
			break;
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

	long int buffer_size = BUF_SIZE;
	if (size != NULL)
	{
		buffer_size = get_value(size);
		if (buffer_size < 0)
		{
			exit(1);
		}
	}

	printf("Reading data from disk %s with buffer size %ld\n", disk, buffer_size);

	for (;;)
	{
		app(disk, buffer_size);
		sleep(1);
	}

	return 0;
}