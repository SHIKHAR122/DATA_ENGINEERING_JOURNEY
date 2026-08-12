 // LEETCODE PROBLEM NUMBER 21 - MERGE TWO SORTED LISTS

 // In this problem, we use two pointers, p1 and p2, each pointing to the head of their respective lists.
 // We compare the values of both nodes and attach the smaller node to the result list.
 // A dummy node is used as a starting point for the result list, making insertion easier.
 // We move the pointer of the list whose node was selected and continue until one list is exhausted.
 // Finally, we attach the remaining nodes of the other list to the result.
 // The dummy node is not part of the answer; we return dummy->next.
 //
 // TIME COMPLEXITY: O(n + m)
 // SPACE COMPLEXITY: O(1) EXTRA SPACE



 class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode(-1);
        ListNode* temp = dummy;
        ListNode* p1 = list1;
        ListNode* p2 = list2;
        while(p1 != nullptr && p2 != nullptr)
        {
            if(p1->val >= p2->val)
            {
                temp->next = p2;
                p2 = p2->next;
            }
            else
            {
                temp->next = p1;
                p1 = p1->next;
            }
            temp = temp->next;
        }
        while(p1 != nullptr)
        {
            temp->next = p1;
            p1 = p1->next;
            temp = temp->next;
        }
        while(p2 != nullptr)
        {
            temp->next = p2;
            p2 = p2->next;
            temp = temp->next;
        }
        return dummy->next;
    }
};