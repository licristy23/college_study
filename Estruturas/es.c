#include <stdio.h>
#include <math.h>

int insertion_sort_steps(int n) {
    return 8 * n * n;
}

int merge_sort_steps(int n) {
    return (int)(64 * n * log2(n));
}

int main() {
    int n = 1;
    while (1) {
        int insertion_steps = insertion_sort_steps(n);
        int merge_steps = merge_sort_steps(n);

        if (insertion_steps <= merge_steps) {
            printf("Para n = %d, o Insertion Sort é mais rápido que o Merge Sort.\n", n);
            n++;
        } else {
            break;
        }
    }

    return 0;
}
