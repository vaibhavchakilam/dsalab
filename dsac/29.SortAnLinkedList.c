//29

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

// Function to split linked list into two halves
void splitList(struct Node* head, struct Node** front, struct Node** back) {
    struct Node* slow = head;
    struct Node* fast = head->next;

    while (fast != NULL) {
        fast = fast->next;
        if (fast != NULL) {
            slow = slow->next;
            fast = fast->next;
        }
    }
    *front = head;
    *back = slow->next;
    slow->next = NULL;
}

// Merge two sorted linked lists
struct Node* sortedMerge(struct Node* a, struct Node* b) {
    struct Node* result = NULL;

    if (a == NULL)
        return b;
    else if (b == NULL)
        return a;

    if (a->data <= b->data) {
        result = a;
        result->next = sortedMerge(a->next, b);
    } else {
        result = b;
        result->next = sortedMerge(a, b->next);
    }
    return result;
}

// Merge Sort for linked list
void mergeSort(struct Node** headRef) {
    struct Node* head = *headRef;
    struct Node* a;
    struct Node* b;

    if ((head == NULL) || (head->next == NULL)) {
        return;
    }

    splitList(head, &a, &b);
    mergeSort(&a);
    mergeSort(&b);
    *headRef = sortedMerge(a, b);
}

// Utility function to insert a node
void push(struct Node** headRef, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = *headRef;
    *headRef = newNode;
}

// Utility function to print the linked list
void printList(struct Node* node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

int main() {
    struct Node* head = NULL;

    // Create linked list: 15->10->5->20->3->2
    push(&head, 2);
    push(&head, 3);
    push(&head, 20);
    push(&head, 5);
    push(&head, 10);
    push(&head, 15);

    printf("Linked List before sorting: \n");
    printList(head);

    mergeSort(&head);

    printf("Linked List after sorting: \n");
    printList(head);

    return 0;
}