// LEETCODE PROBLEM NUBER 237  - DELETE NODE IN A LINKED LIST 


// IN THIS PROBLEM WE WILL POINT THE GIVEN NODE'S VALUE TO THE VALUE OF THE NEXT NODE AND THE NEXT OF THE CURRENT NODE 
// WILL POINT TO THE NEXT NODE'S NEXT VAL 


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        node->val=node->next->val;
        node->next=node->next->next;
    }
};