#include <stdio.h>

// Function to perform binary search iteratively
int binarySearch(int arr[], int size, int value) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == value) {
            return mid;
        }
        if (arr[mid] > value) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return -1;
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int size = sizeof(arr) / sizeof(arr[0]);
    int value = 30;
    int result = binarySearch(arr, size, value);
    if (result != -1) {
        printf("%d found at index %d\n", value, result);
    } else {
        printf("%d not found\n", value);
    }
    return 0;
}
