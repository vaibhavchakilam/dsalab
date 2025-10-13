//21
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to push an element onto the stack
void push(Node** top, int data) {
    Node* newNode = createNode(data);
    newNode->next = *top;
    *top = newNode;
}

// Function to pop an element from the stack
int pop(Node** top) {
    if (*top == NULL) {
        printf("Stack underflow\n");
        exit(1);
    }
    Node* temp = *top;
    *top = (*top)->next;
    int data = temp->data;
    free(temp);
    return data;
}

// Function to evaluate a postfix expression
int evaluatePostfix(char* expression) {
    Node* stack = NULL;

    for (int i = 0; expression[i] != '\0'; i++) {
        // If the character is a digit, push it onto the stack
        if (isdigit(expression[i])) {
            push(&stack, expression[i] - '0');
        } 
        // If the character is an operator, pop two elements from the stack, apply the operator, and push the result back
        else {
            int operand2 = pop(&stack);
            int operand1 = pop(&stack);

            switch (expression[i]) {
                case '+': push(&stack, operand1 + operand2); break;
                case '-': push(&stack, operand1 - operand2); break;
                case '*': push(&stack, operand1 * operand2); break;
                case '/': push(&stack, operand1 / operand2); break;
            }
        }
    }
    // The final result will be on the top of the stack
    return pop(&stack);
}

int main() {
    char expression[100];
    printf("Enter a postfix expression: ");
    scanf("%s", expression);

    int result = evaluatePostfix(expression);
    printf("Result = %d\n", result);

    return 0;
}