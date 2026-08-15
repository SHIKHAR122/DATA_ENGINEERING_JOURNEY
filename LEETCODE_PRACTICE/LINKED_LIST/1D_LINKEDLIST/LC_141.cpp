// LEETCODE PROBLEM NUMBER 141 - LINKED LIST CYCLE 


// APPROACH NUMBER 1 -
// IN THIS APPROACH WE WILL BE USING THE VECTOR THAT WILL BE STORING THE VISITED NODES ,
// KEEP A POINTER NAMED CURR ON THE HEAD , KEEP A CHECK IF THE VALUE AT THE CURRENT ALREADY EXISTS IN THE VECTOR- 
//  IF IT DOES NOT EXISTS THEN PUSH IT  IN THE VECTOR ELSE SIMPLY RETURN TRUE , AS IT HAS BEEN ENCOUNTERED IN THE VECTOR WHICH 
// MEANS THAT WE HAVE BEEN IN A CYCLE


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
    bool hasCycle(ListNode *head) {
        ListNode * curr=head;
        if(curr==nullptr) return false;
        vector<ListNode*>visit;
        while(curr!=nullptr)
        {
            
            for(int i=0;i<visit.size();i++)
            {
                if(visit[i]==curr)
                {
                    return true;
                }    
            }
            visit.push_back(curr);
            curr=curr->next;
            
        }
        return false;
    }
};





// APPROACH NUMBER 2 - THIS APPROACH USES THE SAME LOGIC ONLY DIFFERENCE IS THE DATA STRUCTURE - HERE WE HAVE USED AN UNORDERED SET 
// INSTEAD OF A VECTOR TO TACKLE THE SAME NODES


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
    bool hasCycle(ListNode *head) {
        ListNode* curr=head;
        if(curr==nullptr) return false;
        unordered_set<ListNode*>st;
        while(curr!=nullptr)
        {
            for(int i=0;i<st.size();i++)
            {
                if(st.find(curr)!=st.end())
                {
                    return true;
                }
            }
            st.insert(curr);
            curr=curr->next;
        }
        return false;
    }
};




//APPROACH NUMBER 3 THE MOST OPTIMAL APPROACH , IN THIS APPROACH WE HAVE USED THE TWO POINTERS (FAST & SLOW) , WHERE THE FAST 
// MOVES 2 STEPS AND THE SLOW MOVES 1 STEP AT A TIME , IF THEY MEET EACH OTHER THEN DEFINITELY THERE EXISTS A CYCLE 



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
    bool hasCycle(ListNode *head) {
        if(head == nullptr || head->next == nullptr) return false;

        ListNode* fast = head;
        ListNode* slow = head;

        while(fast != nullptr && fast->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast) return true;
        }
        return false;
    }
};
