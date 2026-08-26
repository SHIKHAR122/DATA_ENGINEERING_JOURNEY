// // GFG PROBLEM NUMBER 3 - SORT THE LIST OF 0s , 1s & 2s 
// Given the head of a linked list where nodes can contain values 0s, 1s, and 2s only. 
//Your task is to rearrange the list so that all 0s appear at the beginning, followed by all 1s, and all 2s are placed at the end.



/* Node is defined as
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
    Node* segregate(Node* head) {
        // code here
        Node* onehead=nullptr;
        Node* onetail=nullptr;
        Node* twohead=nullptr;
        Node* twotail=nullptr;
        Node* zerohead=nullptr;
        Node* zerotail=nullptr;
        Node* curr=head;
        while(curr!=nullptr)
        {
            Node* nextNode= curr->next;
            curr->next=nullptr;
            if(curr->data==1)
            {
                if(onehead==nullptr) //first insertion in this node
                {
                    onehead=curr;
                    onetail=curr;
                    
                }
                else
                {
                    onetail->next=curr;
                    onetail=curr;
                }
            }
            else if (curr->data == 0)
            {
                if(zerohead==nullptr)
                {
                    zerohead=curr;
                    zerotail=curr;
                }
                else
                {
                    zerotail->next=curr;
                    zerotail=curr;
                }
            }
            else 
            {
                if(twohead==nullptr)
                {
                    twohead=curr;
                    twotail=curr;
                }
                else
                {
                    twotail->next=curr;
                    twotail=curr;
                }
            }
            curr=nextNode;
        }
        if (zerohead != nullptr)
        {
            if (onehead != nullptr)
            {
                zerotail->next = onehead;
                onetail->next = twohead;
            }
            else
            {
                zerotail->next = twohead;
            }

            return zerohead;
        }
        else if (onehead != nullptr)
        {
            onetail->next = twohead;
            return onehead;
        }
        else
        {
            return twohead;
        }
    
    }
};