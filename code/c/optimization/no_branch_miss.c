#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 1000000

int main() {
    int *arr = malloc(SIZE * sizeof(int));
    if (!arr) return 1;

    srand(time(NULL));
    for (int i = 0; i < SIZE; ++i) {
        arr[i] = rand() % 100;
    }

    int count = 0;
    for (int i = 0; i < SIZE; ++i) {
        count += (arr[i] > 50);  // no actual branch here; result is 0 or 1
    }

    printf("Count: %d\n", count);
    free(arr);
    return 0;
}

