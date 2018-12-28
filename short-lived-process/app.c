#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

void create_process()
{
	// fake I/O with stress (via write()/unlink()).
	char *argv[6] = { "stress", "--timeout", "1", "--hdd", "1", NULL };

	if (fork() == 0) {
		if (execvp("stress", argv) < 0) {
			perror("Exec error");
			_exit(1);
		}
		_exit(0);
	}
}

int main(void)
{
	signal(SIGCHLD,SIG_IGN); // Avoid zombie process.
	int i = 0;
	for (;;) {
		for (i = 0; i < 3; i++) {
			create_process();
		}
		sleep(5);
	}

	wait(NULL);
	return 0;
}