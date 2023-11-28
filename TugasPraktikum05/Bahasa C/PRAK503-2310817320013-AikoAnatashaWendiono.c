#include <stdio.h>

int minimal(int a, int b) {
    return (a < b) ? a : b;
}

int maksimal(int a, int b) {
    while (a > b) {
        return a;
    }
    return b;
}

int main() {
    int N;
    scanf("%d", &N);

    int maks = -100000;
    int minim = 100000;

    for (int i = 0; i < N; i++) {
        int nilai;
        scanf("%d", &nilai);

        maks = maksimal(maks, nilai);
        minim = minimal(minim, nilai);
    }

    printf("%d %d", maks, minim);

    return 0;
}
