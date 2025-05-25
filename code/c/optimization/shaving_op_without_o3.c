#include <stdio.h>
#include <math.h>


int main() {
    int size = 10000;
    double x[size], y[size];
    
    FILE *file = fopen("data.csv", "r");
    double value;
    int count;
    while (!feof(file)) {
        if (fscanf(file, "%lf,", &value) == 1) {
            if (count < size) {
                x[count] = value;
            }
            else {
                y[count - size] = value;
            }
            count++;
        }
    }
    fclose(file);

    double r;
    int total;
    for(int i = 0; i < size; i++) {
        for(int j = 0; j < size; j++) {
            r = (x[i] - x[j])*(x[i] - x[j]) + (y[i] - y[j])*(y[i] - y[j]);
            if (r < 1.0) {
                total++;
            }
        }
    }

    printf("Prob %f\n", ((float)total)/(size*size));
    return 0;
}
