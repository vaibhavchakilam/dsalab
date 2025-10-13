#include <stdio.h>
#define MAX 5

int queue[MAX];
int front = -1, rear = -1;

// Function to enqueue an element
void enqueue(int value) {
    if ((rear + 1) % MAX == front) {
        printf("Queue Overflow\n");
    } else {
        if (front == -1) {
            front = rear = 0;
        } else {
            rear = (rear + 1) % MAX;
        }
        queue[rear] = value;
        printf("%d enqueued to circular queue\n", value);
    }
}

// Function to dequeue an element
void dequeue() {
    if (front == -1) {
        printf("Queue Underflow\n");
    } else {
        printf("%d dequeued from circular queue\n", queue[front]);
        if (front == rear) {
            front = rear = -1;
        } else {
            front = (front + 1) % MAX;
        }
    }
}

// Function to display the circular queue
void display() {
    if (front == -1) {
        printf("Queue is empty\n");
    } else {
        printf("Queue elements: ");
        int i = front;
        while (i != rear) {
            printf("%d ", queue[i]);
            i = (i + 1) % MAX;
        }
        printf("%d\n", queue[rear]);
    }
}

int main() {
    enqueue(10);
    enqueue(20);
    enqueue(30);
    enqueue(40);
    enqueue(50);
    display();
    dequeue();
    display();
    return 0;
}
