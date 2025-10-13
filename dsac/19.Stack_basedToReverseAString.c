#include <stdio.h>
#include <string.h>
#define MAX 100

char stack[MAX];
int top = -1;

// Function to push a character onto the stack
void push(char c) {
    if (top == MAX - 1) {
        printf("Stack Overflow\n");
    } else {
        stack[++top] = c;
    }
}

// Function to pop a character from the stack
char pop() {
    if (top == -1) {
        printf("Stack Underflow\n");
        return '\0';
    } else {
        return stack[top--];
    }
}

// Function to reverse a string using a stack
void reverseString(char str[]) {
    int len = strlen(str);
    for (int i = 0; i < len; i++) {
        push(str[i]);
    }
    for (int i = 0; i < len; i++) {
        str[i] = pop();
    }
}

int main() {
    char str[] = "Hello";
    printf("Original String: %s\n", str);
    reverseString(str);
    printf("Reversed String: %s\n", str);
    return 0;
}
