#include <stdio.h>

int reverse(int a) {
    int b = 0;

    while (a > 0) {
        b = b * 10 + a % 10;
        a /= 10;
    }
    return b;
}

int main() {
    int A, B;
    scanf("%d %d", &A, &B);

    A = reverse(A);
    B = reverse(B);

    int C = A + B;
    printf("%d", reverse(C));

    return 0;
}
