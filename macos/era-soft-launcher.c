#include <limits.h>
#include <mach-o/dyld.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(void)
{
	char executable_path[PATH_MAX];
	char resolved_path[PATH_MAX];
	char script_path[PATH_MAX];
	uint32_t executable_path_size = sizeof(executable_path);
	char *last_separator;

	if (_NSGetExecutablePath(executable_path, &executable_path_size) != 0) {
		fprintf(stderr, "ERA SOFT launcher path is too long.\n");
		return 1;
	}

	if (realpath(executable_path, resolved_path) == NULL) {
		perror("ERA SOFT launcher cannot resolve its path");
		return 1;
	}

	last_separator = strrchr(resolved_path, '/');
	if (last_separator == NULL) {
		fprintf(stderr, "ERA SOFT launcher has an invalid path.\n");
		return 1;
	}
	*last_separator = '\0';

	if (snprintf(
			script_path,
			sizeof(script_path),
			"%s/../Resources/era-soft-launcher.sh",
			resolved_path
		) >= (int)sizeof(script_path)) {
		fprintf(stderr, "ERA SOFT launcher script path is too long.\n");
		return 1;
	}

	execl("/bin/sh", "sh", script_path, (char *)NULL);
	perror("ERA SOFT launcher cannot start its script");
	return 1;
}
