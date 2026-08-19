// LEETCODE PROBLEM NUMBER 142 - LINKED LIST CYCLE II 

//  FOR THIS PROBLEM OUR APPROACH OF TWO POINTER IS FURTHER DIVIDE INTO TWO OTHER SUBPROBLEMS - 

// 1) THE TWO POINTERS MOVE WITH THE SPEED OF - >   SLOW WITH 1 POINTER PER ITERATION AND FAST POINTER 2 POINTER PER ITERATION 
// THEN THEY WILL KEEP MOVING UNTIL FAST == SLOW , THIS CONFIRMS THAT THE CYCLE EXISTS IN THE LINKED LOST , NOW THE NEXT TASK IS TO IDENTIFY THE NODE 
//  FROM WHERE THE CYCLE HAS BEGUN 

// 2) AGAIN THE POINTERS WILL MOVE BUT THIS TIME 1 ITERATION FOR BOTH i.e. , fast=fast->next and slow=slow->next ; 
//   NOW THEY WILL POINT TO THE SAME NODE IF THE CYCLE EXISTS 

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                slow = head;
                while (slow != fast) {
                    slow = slow->next;
                    fast = fast->next;
                }
                return slow;
            }
        }
        return nullptr;
    }
};