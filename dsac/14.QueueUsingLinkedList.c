#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* front = NULL;
struct Node* rear = NULL;

// Function to enqueue an element
void enqueue(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    if (rear == NULL) {
        front = rear = newNode;
    } else {
        rear->next = newNode;
        rear = newNode;
    }
    printf("%d enqueued to queue\n", value);
}

// Function to dequeue an element
void dequeue() {
    if (front == NULL) {
        printf("Queue Underflow\n");
    } else {
        struct Node* temp = front;
        front = front->next;
        if (front == NULL) {
            rear = NULL;
        }
        printf("%d dequeued from queue\n", temp->data);
        free(temp);
    }
}

// Function to display the queue
void display() {
    struct Node* temp = front;
    if (front == NULL) {
        printf("Queue is empty\n");
    } else {
        printf("Queue elements: ");
        while (temp != NULL) {
            printf("%d ", temp->data);
            temp = temp->next;
        }
        printf("\n");
    }
}

int main() {
    enqueue(10);
    enqueue(20);
    enqueue(30);
    display();
    dequeue();
    display();
    return 0;
}
