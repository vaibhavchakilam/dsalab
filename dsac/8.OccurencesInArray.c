#include <stdio.h>

void countOccurrences(int arr[], int size) {
    int count[size];
    
    for (int i = 0; i < size; i++) {
        count[i] = 1;
        for (int j = i + 1; j < size; j++) {
            if (arr[i] == arr[j]) {
                count[i]++;
                arr[j] = -1; // Mark duplicates as -1
            }
        }
    }

    for (int i = 0; i < size; i++) {
        if (arr[i] != -1) {
            printf("%d occurs %d times\n", arr[i], count[i]);
        }
    }
}

int main() {
    int arr[] = {1, 2, 2, 3, 4, 4, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);
    countOccurrences(arr, size);
    return 0;
}
