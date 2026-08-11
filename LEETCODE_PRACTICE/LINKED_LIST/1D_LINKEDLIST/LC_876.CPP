// LEETCODE PROBLEM NUMBER 876 - MIDDLE OF THE LINKED LIST 

//  THE APPROACH TO SOLVE THIS PROBLEM IS BY SIMPLYE USING TWO POINTERS FAST AND SLOW , THE FAST WILL MOVE 2 STEPS
// WHILE THE SLOW MOVES ONLY 1 STEP AND AS SOON AS THE FAST REACHES THE TAIL OF LL , THE SLOW WILL ALWAYS POINTS TO THE 
// MIDDLE ELEMENT , THEN SIMPLY RETURN THE SLOW POINTER NODE 




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
    ListNode* middleNode(ListNode* head) {
        ListNode* slow= head;
        ListNode* fast=head;
        while(fast!=nullptr&&fast->next!=nullptr)
        {
            slow=slow->next;
            fast=fast->next->next;
        }
        return slow;
    }
};