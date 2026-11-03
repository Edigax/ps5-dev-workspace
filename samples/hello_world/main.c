/**
 * PS5 Sample Homebrew: Hello World
 *
 * Demonstrates:
 * - Standard C library initialization with PS5 Payload SDK
 * - Reading process metadata (PID, UID, GID)
 * - Outputting messages to stdout / network socket console
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[]) {
    (void)argc;
    (void)argv;

    printf("==========================================\n");
    printf(" Hello from PlayStation 5 Homebrew!\n");
    printf("==========================================\n");

    pid_t pid = getpid();
    uid_t uid = getuid();
    gid_t gid = getgid();

    printf("[*] Process ID (PID) : %d\n", pid);
    printf("[*] User ID    (UID) : %d\n", uid);
    printf("[*] Group ID   (GID) : %d\n", gid);
    printf("[*] Execution complete.\n");
    printf("==========================================\n");

    return 0;
}
