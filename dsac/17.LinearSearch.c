#include <stdio.h>

// Function to perform linear search
int linearSearch(int arr[], int size, int value) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == value) {
            return i;
        }
    }
    return -1;
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int size = sizeof(arr) / sizeof(arr[0]);
    int value = 30;
    int result = linearSearch(arr, size, value);
    if (result != -1) {
        printf("%d found at index %d\n", value, result);
    } else {
        printf("%d not found\n", value);
    }
    return 0;
}
