// LEETCODE PROBLEM NUMBER 148 - SORT THE LINKED LIST 

// APPROACH NUMBER 1- BRUTE FORCE APPROACH - IN THIS APPROACH WE WILL STORE THE LINKED LIST ELEMENTS INTO A VECTOR
// THEN SORT THAT VECTOR , THEN  AGAIN STORE THE SORTED VECTOR INTO THR LINKED LIST 


class Solution {
public:
    ListNode* sortList(ListNode* head) {

        vector<int> nums;

        ListNode* temp = head;

        while (temp != nullptr) {
            nums.push_back(temp->val);
            temp = temp->next;
        }

        sort(nums.begin(), nums.end());

        if (nums.empty())
            return nullptr;

        ListNode* newHead = new ListNode(nums[0]);
        ListNode* tail = newHead;

        for (int i = 1; i < nums.size(); i++) {
            tail->next = new ListNode(nums[i]);
            tail = tail->next;
        }

        return newHead;
    }
};




// APPROACH NUMBER 2- USING MERGE SORT + RECURSION 


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
    ListNode* FindMiddle(ListNode* head)
    {
        ListNode* fast=head->next;
        ListNode* slow= head;
        while(fast!=nullptr && fast->next!=nullptr)
        {
            fast=fast->next->next;
            slow=slow->next;
        }
        return slow;
    }
    ListNode* mergedList(ListNode* list1 , ListNode* list2)
    {
        ListNode* dummy= new ListNode(-1);
        ListNode* temp=dummy;
        while(list1!=nullptr && list2!=nullptr)
        {
                if(list1->val >= list2->val)
            {
                temp->next=list2;
                temp=list2;
                list2=list2->next;
            }
            else
            {
                temp->next=list1;
                temp=list1;
                list1=list1->next;
            }
        }
        if(list1) temp->next=list1 ;
        else temp->next=list2;
        return dummy->next;
    }
    ListNode* sortList(ListNode* head) {
        if(head==nullptr || head->next==nullptr) return head;
        ListNode* mid= FindMiddle(head);
        ListNode* right = mid->next;
        mid->next=nullptr;
        ListNode* left=head;

        left=sortList(left);
        right=sortList(right);
        return mergedList(left , right);
    }
};