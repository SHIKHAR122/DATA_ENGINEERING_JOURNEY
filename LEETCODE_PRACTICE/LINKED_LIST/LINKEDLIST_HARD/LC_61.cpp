// LEETCODE PROBLEM NUMBER 61 - ROTATE THE LIST

// THE APPROACH TO SOLVE THIS QUESTION IS :- 

// reverse the whole list once , then at the k%n index place a pointer and break the list into two different sublists
// after breaking them reverse both the lists and then  merge them 



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
    ListNode* ReverseList(ListNode* head)
    {
        ListNode*curr=head;
        ListNode*prev=nullptr;
        ListNode*nextNode=nullptr;
        while(curr!=nullptr)
        {
            nextNode=curr->next;
            curr->next=prev;
            prev=curr;
            curr=nextNode;
        }        
        return prev;
    }
    int findSize(ListNode*head)
    {
        int count=0;
        ListNode*curr=head;
        while(curr!=nullptr)
        {
            curr=curr->next;
            count++;
        }
        return count;
    }
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==nullptr||head->next==nullptr) return head;
        int n = findSize(head);
        k=k%n;
        if(k==0) return head;
        head=ReverseList(head);
        ListNode* curr =head;
        for(int i=0;i<k-1;i++)
        {
            curr=curr->next;
        }
        ListNode* nextNode = curr->next;
        curr->next=nullptr;
        head=ReverseList(head);
        nextNode=ReverseList(nextNode);
        ListNode* tail = head;
        while(tail->next!=nullptr)
        {
            tail=tail->next;
        }
        tail->next=nextNode;
        return head;
    }
};