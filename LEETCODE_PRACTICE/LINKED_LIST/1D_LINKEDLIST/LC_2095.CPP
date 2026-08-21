// LEETCODE PROBLEM  NUMBER 2095 - DELETE THE MIDDLE NODE OF A LINKED LIST

// IN THIS PROBLEM WE WILL BE SOLVING USING THIS APPROACH -

// /FIND THE LENGTH OF THE LINKED LIST → CALCULATE THE MIDDLE POSITION → TRAVERSE TO THE MIDDLE WHILE KEEPING A PREV POINTER → LINK PREV->NEXT TO MIDDLE->NEXT TO SKIP THE MIDDLE NODE → DELETE THE MIDDLE NODE → RETURN HEAD.



class Solution {
public:
    int Length(ListNode* head )
    {
        ListNode* curr= head;
        int count=0;
        while(curr!=nullptr)
        {
            count++;
            curr=curr->next;
        }
        return count;
    }
    ListNode* deleteMiddle(ListNode* head) {
        int length = Length(head);
        int position = length/2;
        ListNode* ptr = head;
        ListNode* prev = nullptr;
        if(head==nullptr||head->next==nullptr) return nullptr;
        for(int i = 0; i < position; i++)
        {
            prev = ptr;
            ptr = ptr->next;
        }
            prev->next=ptr->next;
            delete ptr;
            return head;
    }
};