#define _GNU_SOURCE
#define BUF_SIZE 32*1024*1024

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <sys/file.h>
#include <sys/time.h>

const char *disk = "/dev/sda1";

void app()
{
	int flags = O_RDONLY | O_LARGEFILE;
	int fd = open(disk, flags, 0755);
	if (fd < 0) {
		perror("failed to open disk");
		_exit(1);
	}

	unsigned char *buf;
	struct timeval start, end;
	posix_memalign((void **) &buf, 512, BUF_SIZE);
	int read_bytes = 0;
	gettimeofday(&start, NULL);
	while (read_bytes < BUF_SIZE) {
		int ret = read(fd, buf, BUF_SIZE);
		if (ret < 0) {
			perror("failed to read contents");
			close(fd);
			free(buf);
			_exit(1);
		}
		read_bytes += ret;
	}

	gettimeofday(&end, NULL);
	double total_time = (end.tv_sec - start.tv_sec) + (end.tv_usec - start.tv_usec) / 1000000.0;
	printf("Time used: %f s\n", total_time);
	close(fd);
	free(buf);
}

int main(void)
{
	int status = 0;
	for (;;) {
		app();
		sleep(1);
	}

	return 0;
}