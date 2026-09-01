//  GFG PROBLEM NUMBER 7 - REMOVE DUPLICATES FROM THE SORTED DOUBLY LINKED LIST 


//  THE APPROACH TO SOLVE THIS PROBLEM IS - 

// STEP 1 -  MAKE A NODE POINTER THAT POINTS TO THE HEAD OF THE LIST 
// STEP 2 - CHECK IF THE CURR->NEXT->DATA IS EQUAL TO THE DATA OF THE CURRENT NODE 
// STEP 3 - IF THE DATA IS EQUAL THEN SIMPLY DELETE THE DUPLICATE NODE (DONT MOVE THE CURRENT POINTER)
// STEP 4 - ALSO HANDLE THE EDGE CASES i.e., THE CURR->NEXT SHOULD NOT BE NULLPTR
// STEP 5 - NOW SIMPLY MOVE THE CURRENT POINTER AND RETURN THE HEAD OF THE LINKED LIST 



/* Structure of a link list node
class Node {
  public:
    int data;
    Node* next;
    Node* prev;
    Node(int value) {
        data = value;
        next = nullptr;
        prev = nullptr;
    }
};
*/
class Solution {
  public:
    Node* removeDuplicates(Node* headRef) {
        // code here
        Node * curr = headRef;
        while(curr!=nullptr && curr->next!=nullptr)
        {
            if(curr->data == curr->next->data )
            {
                Node * duplicate = curr->next;
                curr->next=duplicate->next;
                if(curr->next!=nullptr)
                {
                    duplicate->next->prev=duplicate->prev;
                }
                delete duplicate;
            }
            else
            {
                curr=curr->next;
            }
        }
        return headRef;
    }
};


// TIME COMPLEXITY - O(N)
// SPACE COMPLEXITY - O(1)


