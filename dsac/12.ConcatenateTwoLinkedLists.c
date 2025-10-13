#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* head1 = NULL;
struct Node* head2 = NULL;

// Function to insert a node at the end of a list
void insert(struct Node** head, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    
    if (*head == NULL) {
        *head = newNode;
    } else {
        struct Node* temp = *head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

// Function to concatenate two linked lists
void concatenate(struct Node** head1, struct Node* head2) {
    if (*head1 == NULL) {
        *head1 = head2;
        return;
    }
    struct Node* temp = *head1;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = head2;
}

// Function to display a linked list
void display(struct Node* head) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    insert(&head1, 10);
    insert(&head1, 20);
    insert(&head1, 30);
    insert(&head2, 40);
    insert(&head2, 50);
    insert(&head2, 60);
    
    printf("List 1: ");
    display(head1);
    printf("List 2: ");
    display(head2);
    
    concatenate(&head1, head2);
    printf("Concatenated list: ");
    display(head1);
    
    return 0;
}
