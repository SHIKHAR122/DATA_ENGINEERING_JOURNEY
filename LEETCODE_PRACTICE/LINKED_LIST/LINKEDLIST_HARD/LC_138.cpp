// LEETCODE PROBLEM NUMBER 138 - COPY LIST WITH RANDOM POINTER

// APPROACH NUMBER  1 USING THE HASH MAP 
// in this approach we will use hashmap to store the key value pair of original index and the dummy index
// after storing them , we will create a copy linked list  , and simply use  the hashmap relation to point the random and next pointer in the list 

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node* , Node*>mp;
        Node* temp= head;
        while(temp!=nullptr)
        {
            Node* dummyNode = new Node(temp->val);
            mp[temp]=dummyNode;
            temp=temp->next;
        }
        temp=head;
        while(temp!=nullptr)
        {
            Node* copy  = mp[temp];
            copy->next=mp[temp->next];
            copy->random=mp[temp->random];
            temp=temp->next;
        }
        return mp[head];
    }
};

// THE ABOVE APPROACH WILL TAKE O(N) TIME COMPLEXITY AND A O(N) SPACE COMPLEXITY AS WELL , ALSO WE CAN OPTIMIZE THIS APPROACH 

// OPTIMAL APPROACH FOR THIS PROBLEM - 
// INSTEAD OF USING EXTRA SPACE COMPLEXITY , WE CAN MAKE THE INPLPACE MODIFICATIONS TO MAKE IT OPTIMAL FOR THAT WE WILL SIMPLYFOLLOW THESE STEPS


// 1. PHASE 1 (INTERLEAVE): CREATE A CLONED NODE FOR EACH ORIGINAL NODE AND INSERT IT IMMEDIATELY AFTER THE ORIGINAL NODE (TEMP->NEXT = CURR, CURR->NEXT = TEMP->NEXT).

// 2. ADVANCE TEMP BY ONE HOP (TEMP = CURR->NEXT) TO PROCEED TO THE NEXT ORIGINAL NODE.

// 3. PHASE 2 (RANDOM POINTERS): RESET TEMP TO HEAD. SET EACH CLONED NODE'S RANDOM POINTER TO POINT TO THE CLONED VERSION OF THE ORIGINAL RANDOM TARGET (TEMP->NEXT->RANDOM = TEMP->RANDOM->NEXT).

// 4. ADVANCE TEMP BY TWO HOPS (TEMP = TEMP->NEXT->NEXT) TO SKIP THE CLONED NODES.

// 5. PHASE 3 (UNWEAVE): RESET TEMP TO HEAD AND INITIALIZE A DUMMY NODE WITH A TRACKING POINTER (RES) TO BUILD THE CLONED LIST.

// 6. EXTRACT THE CLONED NODE (RES->NEXT = TEMP->NEXT), RESTORE THE ORIGINAL LIST'S LINK (TEMP->NEXT = TEMP->NEXT->NEXT), AND MOVE BOTH RES AND TEMP FORWARD TO SEPARATE THE TWO LISTS IN-PLACE.

// 7. RETURN DUMMY->NEXT AS THE HEAD OF THE COPIED LINKED LIST.



/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {//creating the link bw original and the copy nodes
        if(head==nullptr) return nullptr;
        Node* temp=head;
        while(temp!=nullptr)
        {
            Node* curr=new Node(temp->val);
            curr->next=temp->next;
            temp->next=curr;
            temp=curr->next;
        }
        temp=head;
        while (temp != nullptr) {
        if (temp->random != nullptr) {
            temp->next->random = temp->random->next;
        } else {
            temp->next->random = nullptr;
        }
        temp = temp->next->next;
        }
        //step 3 is to make the next pointer point 
        Node* dummy = new Node(-1);
        Node* res = dummy;
        temp=head;
        while (temp != nullptr) {
            Node* clonedNode = temp->next;
            res->next = clonedNode;
            res = res->next;
            temp->next = clonedNode->next;
            temp = temp->next;
        }
        return dummy->next;
            }
        };