#include <stdio.h>

// Function to find minimum and maximum elements in an array
void findMinMax(int arr[], int size) {
    int min = arr[0], max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    printf("Minimum: %d\n", min);
    printf("Maximum: %d\n", max);
}

int main() {
    int arr[] = {10, 20, 5, 30, 15};
    int size = sizeof(arr) / sizeof(arr[0]);
    findMinMax(arr, size);
    return 0;
}
