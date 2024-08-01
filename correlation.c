#include <stdio.h>
#include <complex.h>

double complex correlate(double complex *reference, double complex *signal, int length) {
    double complex result = 0;
    for (int i = 0; i < length; i++) {
        result += reference[i] * conj(signal[i]);
    }
    return result;
}

int main() {
    double complex reference[] = {20.674737216576254 - 1024.369780669487 * I};
    double complex signal[] = {20.674737216576254-1024.369780669487 * I};
    int length = sizeof(signal) / sizeof(signal[0]);

    double complex result = correlate(reference, signal, length);
    printf("Correlation result: %f + %fi\n", creal(result), cimag(result));
    return 0;
}
