// LEETCODE PROBLEM NUMBER 25 - REVERESE NODES IN K GROUPS 


// Approach: Find kth node → isolate group → reverse → reconnect

// Start with temp = head and prev = nullptr.
// Find the kth node from temp.
// If fewer than k nodes remain → leave them unchanged and stop.
// Store nextNode = kthNode->next.
// Break the group: kthNode->next = nullptr.
// Reverse the current group using the standard iterative linked-list reversal.
// Connect the reversed group:
// First group → update head = kthNode
// Other groups → prev->next = kthNode
// prev = temp because the original first node becomes the tail after reversal.
// temp = nextNode and repeat.


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* temp)
    {
        ListNode* curr = temp;
        ListNode* prev = nullptr;
        ListNode* nextNode= nullptr;
        while(curr!=nullptr)
        {
            nextNode = curr->next;
            curr->next=prev;
            prev=curr;
            curr=nextNode;
        }
        return prev;
    }
    ListNode* GetKthNode(ListNode* temp , int k ){
        // ListNode* curr = head;
            while(k>1 && temp!=nullptr)
            {  
                
                temp=temp->next;
                k--; 
            }
            return temp;
    }
    
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* temp=head;
        ListNode* prev= nullptr;
        while(temp!=nullptr)
        {
            ListNode* kthNode = GetKthNode(temp , k);
            if(kthNode == nullptr)
            {
                if(prev)
                {
                    prev->next=temp;
                    break;
                }
                
            }
           ListNode* nextNode= kthNode->next;
           kthNode->next=nullptr;
           reverseList(temp);
           if(head==temp)
           {
                head=kthNode;
           }
           else
           {
              prev->next=kthNode;
              
           }
           prev=temp;
           temp=nextNode;
        }
        return head;
    }
};