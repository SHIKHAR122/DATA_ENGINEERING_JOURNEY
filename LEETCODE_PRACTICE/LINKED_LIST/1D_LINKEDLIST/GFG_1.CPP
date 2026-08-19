//  GFG QUESTION 
//  FIND THE LENGTH OF THE CYCLE IN A LINKED LIST 


// APPROACH NUMBER 1 - USING A HASH MAP 
// Traverse the linked list while storing each node’s first index in a hashmap; when a node repeats,
// current index − first index gives the loop length.




/* Structure of Linked List Node
class Node {
 public:
    int data;
    Node *next;
    Node(int x) {
        data = x;
        next = nullptr;
    }
};*/

class Solution {
  public:
    int lengthOfLoop(Node *head) {
        int length=0;
        int count=0;
        Node* temp = head;
        unordered_map<Node* , int>mp;
        while(temp!=nullpatr)
        {
            
            if(mp.find(temp)!=mp.end())
            {
                length=count-mp[temp];
                
            }
           mp[temp]=count;
           temp=temp->next;
           count++;
        }
        return length; 
       
    }
};