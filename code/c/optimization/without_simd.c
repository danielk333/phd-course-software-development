void add_float_arrays(float* a, float* b, float* result, int size) {
    for (int i = 0; i < size; ++i) {
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

    add_float_arrays(x, y, res, size);
    for (int i = 0; i < steps; i++) {
        add_float_arrays(res, y, res, size);
    }
    return 0;
}
