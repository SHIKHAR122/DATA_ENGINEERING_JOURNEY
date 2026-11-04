// GFG PROBLEM - STACK IMPLEMENTATION USING LINKED LIST 
#include<bits/stdc++.h>
using namespace std;

/* Structure of linked list Node
class Node {
  public:
    int data;
    Node* next;

    Node(int val) {
        data = val;
        next = nullptr;
    }
};*/

class myStack {
    Node* head;
    int count;

  public:
    myStack() {
        // Initialize your data members
        head=nullptr;
        count=0;
    }

    bool isEmpty() {
        // check if the stack is empty
        return head==nullptr;
    }

    void push(int x) {
        // Adds an element x at the top of the stack
        Node* newNode= new Node(x);
        newNode->next=head;
        head=newNode;
        count++;
    }

    void pop() {
        // Removes the top element of the stack
        Node* temp= head;
        head=head->next;
        delete temp;
        count--;
    }

    int peek() {
        // Returns the top element of the stack
        // If stack is empty, return -1
        if(head==nullptr){
            return -1;
        }
        return head->data;
    }

    int size() {
        // Returns the current size of the stack
        return count;
    }
};

int main()
{
    myStack st;

    // Check initially empty stack
    cout << "Is Empty: " << st.isEmpty() << endl;

    // Push elements
    st.push(10);
    st.push(20);
    st.push(30);

    cout << "Top Element: " << st.peek() << endl;
    cout << "Stack Size: " << st.size() << endl;

    // Remove the top element
    st.pop();

    cout << "\nAfter pop operation:" << endl;
    cout << "Top Element: " << st.peek() << endl;
    cout << "Stack Size: " << st.size() << endl;

    // Push another element
    st.push(40);

    cout << "\nAfter pushing 40:" << endl;
    cout << "Top Element: " << st.peek() << endl;
    cout << "Stack Size: " << st.size() << endl;

    // Remove all elements
    st.pop();
    st.pop();
    st.pop();

    cout << "\nAfter removing all elements:" << endl;
    cout << "Is Empty: " << st.isEmpty() << endl;
    cout << "Top Element: " << st.peek() << endl;

    return 0;
}