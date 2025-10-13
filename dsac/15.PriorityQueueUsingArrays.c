#include <stdio.h>
#define MAX 5

int queue[MAX];
int size = 0;

// Function to insert elements in a priority queue (in sorted order)
void enqueue(int value) {
    if (size == MAX) {
        printf("Priority Queue Overflow\n");
        return;
    }
    int i = size - 1;
    while (i >= 0 && queue[i] > value) {
        queue[i + 1] = queue[i];
        i--;
    }
    queue[i + 1] = value;
    size++;
    printf("%d enqueued to priority queue\n", value);
}

// Function to dequeue the highest priority element (smallest value)
void dequeue() {
    if (size == 0) {
        printf("Priority Queue Underflow\n");
    } else {
        printf("%d dequeued from priority queue\n", queue[0]);
        for (int i = 0; i < size - 1; i++) {
            queue[i] = queue[i + 1];
        }
        size--;
    }
}

// Function to display the priority queue
void display() {
    if (size == 0) {
        printf("Priority Queue is empty\n");
    } else {
        printf("Priority Queue elements: ");
        for (int i = 0; i < size; i++) {
            printf("%d ", queue[i]);
        }
        printf("\n");
    }
}

int main() {
    enqueue(30);
    enqueue(20);
    enqueue(10);
    display();
    dequeue();
    display();
    return 0;
}
