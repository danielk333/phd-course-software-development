#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    char *p;
    long num;
    num = strtol(argv[1], &p, 10);

    printf("Hello %d\n", num);
    return 0;
}
