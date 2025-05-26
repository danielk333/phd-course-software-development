#include <immintrin.h>

void add_float_arrays_avx512(const float* a, const float* b, float* result, int size) {
    int i;
    for (i = 0; i <= size - 16; i += 16) {
        __m512 va = _mm512_loadu_ps(&a[i]);
        __m512 vb = _mm512_loadu_ps(&b[i]);
        __m512 vsum = _mm512_add_ps(va, vb);
        _mm512_storeu_ps(&result[i], vsum);
    }
    for (; i < size; ++i) {
        result[i] = a[i] + b[i];
    }
}

int main() {
    int size = 100000;
    int steps = 1000;
    float x[size], y[size], res[size];

    for (int i = 0; i < size; i++) {
        x[i] = (float)i;
        y[i] = x[i] + 1;
    }

    add_float_arrays_avx512(x, y, res, size);
    for (int i = 0; i < steps; i++) {
        add_float_arrays_avx512(res, y, res, size);
    }
    return 0;
}
