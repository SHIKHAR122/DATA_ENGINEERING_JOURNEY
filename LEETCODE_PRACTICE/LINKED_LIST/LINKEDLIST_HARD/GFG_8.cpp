// GFG PROBLEM NUMBER 8 FLATTENING A LINKED LIST 


// APPROACH NUMBER 1 - 
// BRUTE FORCE APPROACH - IN THIS APROACH WE WILL TRAVERSE THE LINKED LIST AND THEN STORE THEM IN A VECTOR THEN SORT THE VECTOR 
// AND AT LAST , PRINT THE SORTED VECTOR AS A LINKED LIST 

//  TIME COMPLEXITY FOR THIS APPROACH IS O(n log n)
// SPACE COMPLEXITY FOR THIS APPROACH IS 0(N)


/* Structure of Linked List Node
class Node {
public:
    int data;
    Node* next;
    Node* bottom;

    Node(int x) {
        data = x;
        next = nullptr;
        bottom = nullptr;
    }
};*/

class Solution {
  public:
    Node* flatten(Node* head) {
        // code here
        vector<int>nums;
        Node* curr = head;
        if(head==nullptr) return nullptr;
        while(curr!=nullptr)
        {
            Node* bottomptr=curr;
            while(bottomptr!=nullptr)
            {
                nums.push_back(bottomptr->data);
                bottomptr=bottomptr->bottom;
            }
            curr=curr->next;
        }
        sort(nums.begin() , nums.end());
        Node*dummy = new Node (-1);
        Node* current = dummy;
        for(auto val : nums)
        {
            current->bottom=new Node(val);
            current=current->bottom;
        }
        return dummy->bottom;
    }
};




// APPROACH NUMBER 2 USING THE HELPER FUNCTION 

