#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 1000000

// perf record --all-user -e branch-misses
int main() {
    int *arr = malloc(SIZE * sizeof(int));
    if (!arr) return 1;

    srand(time(NULL));
    for (int i = 0; i < SIZE; ++i) {
        arr[i] = rand() % 100;
    }

    int count = 0;
    for (int i = 0; i < SIZE; ++i) {
        if (arr[i] > 50) { // unpredictable branch
            count++;
        }
    }

    printf("Count: %d\n", count);
    free(arr);
    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 10000000

int do_something(int x) {
    // Costly function to exaggerate branch misprediction penalty
    volatile int sum = 0;
    for (int i = 0; i < 10; ++i)
        sum += x * i;
    return sum;
}

int do_something_else(int x) {
    volatile int sum = 1;
    for (int i = 1; i < 10; ++i)
        sum *= (x + i);
    return sum;
}

int main() {
    int *arr = malloc(SIZE * sizeof(int));
    if (!arr) return 1;

    srand(time(NULL));
    for (int i = 0; i < SIZE; ++i) {
        arr[i] = rand();
    }

    volatile int dummy = 0;
    for (int i = 0; i < SIZE; ++i) {
        if (arr[i] % 2 == 0) {
            dummy += do_something(arr[i]);
        } else {
            dummy += do_something_else(arr[i]);
        }
    }

    printf("Dummy result: %d\n", dummy);
    free(arr);
    return 0;
}
int main() {
    int *arr = malloc(SIZE * sizeof(int));
    if (!arr) return 1;

    srand(time(NULL));
    for (int i = 0; i < SIZE; ++i) {
        arr[i] = rand();
    }

    volatile int dummy = 0;
    for (int i = 0; i < SIZE; ++i) {
        int is_even = !(arr[i] % 2);  // 1 if even, 0 if odd

        // Always call both, but select result based on `is_even`
        int a = do_something(arr[i]);
        int b = do_something_else(arr[i]);
        dummy += is_even * a + (!is_even) * b;
    }

    printf("Dummy result: %d\n", dummy);
    free(arr);
    return 0;
}

