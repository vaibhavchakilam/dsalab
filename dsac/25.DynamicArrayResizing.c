//25
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;            // Pointer to hold the dynamic array
    int size = 0;       // Current size of the array
    int capacity = 2;   // Initial capacity of the array
    int input;          // Variable to hold user input

    // Allocate initial memory for the array
    arr = (int *)malloc(capacity * sizeof(int));
    if (arr == NULL) {
        printf("Memory allocation failed!\n");
        return 1; // Exit if memory allocation fails
    }

    printf("Enter integers (enter -1 to stop):\n");

    while (1) {
        scanf("%d", &input);
        if (input == -1) {
            break; // Exit loop if user enters -1
        }

        // Check if we need to resize the array
        if (size == capacity) {
            capacity *= 2; // Double the capacity
            arr = (int *)realloc(arr, capacity * sizeof(int));
            if (arr == NULL) {
                printf("Memory reallocation failed!\n");
                return 1; // Exit if reallocation fails
            }
        }

        arr[size++] = input; // Add the new element and increase size
    }

    // Print the contents of the array
    printf("The elements in the dynamic array are:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Free the allocated memory
    free(arr);

    return 0;
}