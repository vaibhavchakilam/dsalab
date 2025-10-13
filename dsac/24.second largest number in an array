//24 
#include <stdio.h>

int main() {
    int n, i, largest, secondLargest;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    if (n < 2) {
        printf("Array should have at least two elements.\n");
        return 1;
    }

    int arr[n]; // Declare the array

    printf("Enter the elements:\n");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    largest = secondLargest = -2147483648; // Initialize to a very small number

    for (i = 0; i < n; i++) {
        if (arr[i] > largest) {
            secondLargest = largest; // Update second largest
            largest = arr[i];        // Update largest
        } else if (arr[i] > secondLargest && arr[i] != largest) {
            secondLargest = arr[i];  // Update second largest
        }
    }

    if (secondLargest == -2147483648) {
        printf("No second largest element found.\n");
    } else {
        printf("The second largest element is: %d\n", secondLargest);
    }

    return 0;
}