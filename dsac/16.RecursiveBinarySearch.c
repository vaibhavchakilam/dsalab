#include <stdio.h>

// Function to perform binary search recursively
int binarySearch(int arr[], int left, int right, int value) {
    if (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == value) {
            return mid;
        }
        if (arr[mid] > value) {
            return binarySearch(arr, left, mid - 1, value);
        }
        return binarySearch(arr, mid + 1, right, value);
    }
    return -1;
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int size = sizeof(arr) / sizeof(arr[0]);
    int value = 30;
    int result = binarySearch(arr, 0, size - 1, value);
    if (result != -1) {
        printf("%d found at index %d\n", value, result);
    } else {
        printf("%d not found\n", value);
    }
    return 0;
}
