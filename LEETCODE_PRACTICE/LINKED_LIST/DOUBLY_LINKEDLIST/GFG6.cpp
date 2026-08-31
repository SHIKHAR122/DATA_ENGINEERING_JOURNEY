// GFG PROBLEM NUMBER 6 - PAIR SUM IN SORTED DOUBLY LINKED LIST 

// THIS PROBLEM CAN BE SOLVED USING THE 2 POINTERS APPROACH 

// APPROACH NUMBER 1 -
//********** */ CONVERGING / OPPOSITE-END TWO POINTERS ********************
// START HEAD AT THE BEGINNING AND TAIL AT THE END, MOVE HEAD FORWARD OR TAIL BACKWARD BASED ON THE SUM UNTIL THEY MEET — O(N).


/* Structure of Doubly Linked List Node
class Node {
  public:
    int data;
    Node *next;
    Node *prev;

    Node(int val) {
        data = val;
        next = nullptr;
        prev = nullptr;
    }
}; */

class Solution {
  public:
    vector<vector<int>> givenSumPairs(Node* head, int target) {
        vector<vector<int>> ans;
        
        Node* tail=head;
        while(tail->next!=nullptr)
        {
            tail=tail->next;
        }
        while(head->data < tail->data)
        {
            int sum= head->data + tail->data; 
            if(sum==target)
            {
                ans.push_back({head->data , tail->data});
                head=head->next;
                tail=tail->prev;
            }
            else if(sum>target)
            {
                tail=tail->prev;
            }
            else
            {
                head=head->next;
            }
        }
        return ans;
        
    }
};

// APPROACH NUMBER 2 
// 2. *****************PAIR ENUMERATION / NESTED TWO POINTERS****************************
// KEEP HEAD FIXED, MOVE TAIL THROUGH ALL NODES AFTER IT, THEN MOVE HEAD FORWARD AND RESET TAIL, CHECKING EVERY POSSIBLE PAIR — O(N²).

/* Structure of Doubly Linked List Node
class Node {
  public:
    int data;
    Node *next;
    Node *prev;

    Node(int val) {
        data = val;
        next = nullptr;
        prev = nullptr;
    }
}; */



/* Structure of Doubly Linked List Node
class Node {
  public:
    int data;
    Node *next;
    Node *prev;

    Node(int val) {
        data = val;
        next = nullptr;
        prev = nullptr;
    }
}; */

class Solution {
  public:
    vector<vector<int>> givenSumPairs(Node* head, int target) {
        // code here
        vector<vector<int>>ans;
        if(head==nullptr) return ans;
        Node* ptr1= head;
        while(ptr1!=nullptr)
        {
            Node* ptr2 = ptr1->next;
            while(ptr2!=nullptr)
            {
                int sum=ptr1->data + ptr2->data;
                if(sum==target)
                {
                    ans.push_back({ptr1->data , ptr2->data});
                }
                ptr2=ptr2->next;
            }
            ptr1=ptr1->next;
        }
        return ans;
    }
};