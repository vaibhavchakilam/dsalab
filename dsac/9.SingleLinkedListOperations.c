#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* head = NULL;

// Function to insert a node at the end of the list
void insert(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    if (head == NULL) {
        head = newNode;
    } else {
        struct Node* temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
    printf("%d inserted into list\n", value);
}

// Function to delete a node with a specific value
void delete(int value) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    struct Node* temp = head;
    struct Node* prev = NULL;
    if (temp != NULL && temp->data == value) {
        head = temp->next;
        free(temp);
        printf("%d deleted from list\n", value);
        return;
    }
    while (temp != NULL && temp->data != value) {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL) {
        printf("%d not found in list\n", value);
        return;
    }
    prev->next = temp->next;
    free(temp);
    printf("%d deleted from list\n", value);
}

// Function to search for a node in the list
void search(int value) {
    struct Node* temp = head;
    while (temp != NULL) {
        if (temp->data == value) {
            printf("%d found in list\n", value);
            return;
        }
        temp = temp->next;
    }
    printf("%d not found in list\n", value);
}

// Function to display the list
void display() {
    struct Node* temp = head;
    if (temp == NULL) {
        printf("List is empty\n");
        return;
    }
    printf("List elements: ");
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    insert(10);
    insert(20);
    insert(30);
    display();
    search(20);
    delete(20);
    display();
    return 0;
}
