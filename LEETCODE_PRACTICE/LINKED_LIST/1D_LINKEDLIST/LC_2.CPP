//  LEETCODE PROBLEM NUMBER 2 - ADD TWO NUMBERS 

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* curr1 = l1;
        ListNode* curr2 = l2;
        ListNode* dummy= new ListNode(0);
        int sum=0;
        int carry=0;
        ListNode* curr = dummy;
        while(curr1!=nullptr && curr2!=nullptr && carry!=0)
        {
            sum=carry;
            if(curr!=nullptr)
            {
                sum+=curr1->val;
                curr1=curr1->next;
            }
            if(curr2!=nullptr)
            {
                sum+=curr2->val;
                curr2=curr2->next;
            }
            int digit=sum%10;
            carry=sum/10;

            curr->next=new ListNode(digit);
            curr=curr->next;   
        }
        return dummy->next;
    }
};