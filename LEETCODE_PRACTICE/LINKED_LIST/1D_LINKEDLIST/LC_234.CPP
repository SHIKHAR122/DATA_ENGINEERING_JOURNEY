// LEETCODE PROBLEM NUMBER 234 - PALINDROME LINKED LIST 

// APPROACH NUMBER 1 - IN THIS APPROACH WE TRIED TO SOLVE THE PALINDROME USING THE STACK DATA STRUCTURE THROUGH THESE STEPS : - 
//  1- PUSH ALL THE NODES IN THE STACK 
//  2- KEEP A POINTER AT THE HEAD WHICH CHECKS IF THE HEAD VALUE IS EQUAL TO THE ST.TOP()->VAL
//  3 - ACCODINGLY RETURN THE RESULT 


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
    bool isPalindrome(ListNode* head) {
        if(!head||!head->val) return true;
        ListNode* ptr=head;
        stack<ListNode*>st;
        while(ptr!=nullptr)
        {
            st.push(ptr);
            ptr=ptr->next;
        }
        ptr=head;
        while(ptr!=nullptr)
        {
            if(ptr->val!=st.top()->val)
            {
                return false;
            }   
            st.pop();
            ptr=ptr->next;
        }
        return true;
    }   
};