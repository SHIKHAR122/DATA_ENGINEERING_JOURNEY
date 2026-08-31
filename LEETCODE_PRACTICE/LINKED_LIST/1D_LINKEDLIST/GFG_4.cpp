//  GFG PROBLEM NUMBER 4 - ADD 1 TO THE LINKED LIST 

//  THIS PROBLEM CAN BE SOLVED USING 2 APPROACHES - 

// APPROACH NUMBER 1-   ITERATIVE APPROACH 

// IN THIS APPROACH THE PROCESS TO SOLVE THE QUESTION IS AS FOLLOWED - 

// Reverse the list and start from the head and add 1. Carry it forward as needed.
// If a carry remains after the last node, add a new node with value 1.
// Reverse the list again to restore the original order and return the head of the modified list.



/* Structure of linked list Node
class Node {
public:
    int data;
    Node* next;

    Node(int x) {
        data = x;
        next = nullptr;
    }
};
*/
class Solution {
  public:
    Node* reverseList(Node* head)
    {
        Node* prev = nullptr ; 
        Node* curr = head;
        Node* nextNode ;
        while(curr!=nullptr)
        {
            nextNode = curr->next;
            curr->next=prev;
            prev=curr;
            curr= nextNode;
        }
        return prev;
    }
    Node* addOne(Node* head) {
        head=reverseList(head);
        
        Node* curr = head;
        int sum=0;
        int carry=1;
        while(curr && head)
        {
            sum=curr->data+ carry;
            curr->data=sum%10;
            carry=sum/10;
            if (!curr->next && carry) {
                    curr->next = new Node(carry);
                    carry = 0;  
                }

                curr = curr->next;
            }

            head = reverseList(head);
            return head;
        } 
    
};






