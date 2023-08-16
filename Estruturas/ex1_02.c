#include <stdio.h>

void  insertionSort(int A[],int n){
    int key, j, i;
    for(i=1; i < n; i++){
        key = A[i];

        j = i - 1;

        while(j > 0 && A[j] <  key){
            A[j + i] = A[j];
            j = j - i;
        }
        A[j + 1] =key;
    }

}