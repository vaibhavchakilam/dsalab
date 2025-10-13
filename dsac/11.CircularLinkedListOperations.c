#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* head = NULL;

// Function to insert a node at the end
void insert(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    
    if (head == NULL) {
        head = newNode;
        newNode->next = head;
    } else {
        struct Node* temp = head;
        while (temp->next != head) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->next = head;
    }
    printf("%d inserted into circular list\n", value);
}

// Function to delete a node with a specific value
void delete(int value) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    
    struct Node* temp = head;
    struct Node* prev = NULL;

    if (temp->data == value) {
        if (temp->next == head) { 
            free(temp);
            head = NULL;
        } else {
            struct Node* last = head;
            while (last->next != head) {
                last = last->next;
            }
            last->next = temp->next;
            head = temp->next;
            free(temp);
        }
        printf("%d deleted from circular list\n", value);
        return;
    }
    
    while (temp->next != head && temp->data != value) {
        prev = temp;
        temp = temp->next;
    }

    if (temp->data == value) {
        prev->next = temp->next;
        free(temp);
        printf("%d deleted from circular list\n", value);
    } else {
        printf("%d not found in circular list\n", value);
    }
}

// Function to display the circular linked list
void display() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    
    struct Node* temp = head;
    printf("Circular list elements: ");
    do {
        printf("%d ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("\n");
}

int main() {
    insert(10);
    insert(20);
    insert(30);
    display();
    delete(20);
    display();
    return 0;
}
