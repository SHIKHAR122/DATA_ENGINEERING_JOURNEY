// LEETCODE PROBLEM NUMBER 19 - DELETE Nth NODE FROM THE END OF THE LIST 


// APPROACH NUMBER 1 - 
// WE HAVE FOLLOWED THIS ALGORITHM TO SOLVE THIS PROBLEM- 


// STEP1 - FIND THE LENGTH OF THE LL

// STEP2 - FIND THE POSITION OF THE NODE WHICH IS TO BE DELETED BY THE FORMULA - (LENGTH OF LL)+N-1  WHERE N IS THE POSITION TO BE DELETD

// STEP3 - TRAVERSE TO THE PREVIOUS NODE OF THE 'N' NODE AND THEN APPLY THE DELETING ALGO



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
    int Length(ListNode* head)
    {
        int count=0;
        ListNode* temp = head;
        while(temp!=NULL)
        {
            count++;
            temp=temp->next;   
        }
        return count;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int length=Length(head); //finding the length of the LL
        int position;
        position=length-n+1;//finding the position whose node has to be removed
        if(position == 1)
        {
            ListNode* temp = head;
            head = head->next;
            delete temp;
            return head;
        } //handling the edge case 
        ListNode* temp = head;
        for(int i=1;i<position-1;i++)
        {
             temp=temp->next;   //Pointing to the previous node to delete the next node 
        }
        ListNode * del=temp->next;
        temp->next=temp->next->next;
        delete del;
        return head;
    }
};