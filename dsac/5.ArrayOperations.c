#include <stdio.h>
#define MAX 10

int arr[MAX];
int size = 0;

// Function to insert an element into the array
void insert(int value, int pos) {
    if (size == MAX) {
        printf("Array is full\n");
        return;
    }
    if (pos < 0 || pos > size) {
        printf("Invalid position\n");
        return;
    }
    for (int i = size; i > pos; i--) {
        arr[i] = arr[i - 1];
    }
    arr[pos] = value;
    size++;
}

// Function to delete an element from the array
void delete(int pos) {
    if (size == 0) {
        printf("Array is empty\n");
        return;
    }
    if (pos < 0 || pos >= size) {
        printf("Invalid position\n");
        return;
    }
    for (int i = pos; i < size - 1; i++) {
        arr[i] = arr[i + 1];
    }
    size--;
}

// Function to search for an element in the array
int search(int value) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == value) {
            return i;
        }
    }
    return -1;
}

// Function to display the array
void display() {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    insert(10, 0);
    insert(20, 1);
    insert(30, 2);
    display();
    delete(1);
    display();
    printf("Search 30: %d\n", search(30));
    return 0;
}
