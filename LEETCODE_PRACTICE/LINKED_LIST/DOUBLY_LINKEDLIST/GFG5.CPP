// GFG PROBLEM NUMBER 5 - DELETE ALL OCCURENCE OF AN ELEMENT X IN THE LINKED LIST

// THIS PROBLEM IS SOLVED USING THIS APPROACH - 

// **TRAVERSE THE DLL, DELETE EVERY NODE WITH VALUE X BY RECONNECTING ITS PREV AND NEXT NODES, AND MOVE USING THE SAVED NEXT POINTER.**



class Solution {
public:
    Node* deleteAllOccurOfX(Node* head, int x) {
        if (head == nullptr)
            return nullptr;
        Node* curr = head;
        while (curr != nullptr)
        {
            Node* nextNode = curr->next;
            if (curr->data == x)
            {
                if (curr == head)
                {
                    head = curr->next;

                    if (head != nullptr)
                        head->prev = nullptr;
                }
                else
                {
                    if (curr->prev != nullptr)
                        curr->prev->next = curr->next;

                    if (curr->next != nullptr)
                        curr->next->prev = curr->prev;
                }
                delete curr;
            }
            curr = nextNode;
        }
        return head;
    }
};