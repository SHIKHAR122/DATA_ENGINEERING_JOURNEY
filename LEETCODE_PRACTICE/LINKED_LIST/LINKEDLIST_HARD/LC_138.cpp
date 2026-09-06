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

