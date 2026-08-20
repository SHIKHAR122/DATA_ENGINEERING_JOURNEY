// // GFG PROBLEM NUMBER 2 SEGREGATE EVEN AND ODD NODES IN A LINKED LIST 

// SEGREGATE EVEN AND ODD NODES — TWO-CHAIN APPROACH

// * TRAVERSE THE ORIGINAL LINKED LIST USING A `CURR` POINTER.
// * MAINTAIN TWO SEPARATE CHAINS USING THE **EXISTING NODES**:

//   * `EVENHEAD` AND `EVENTAIL` FOR EVEN NODES.
//   * `ODDHEAD` AND `ODDTAIL` FOR ODD NODES.
// * IF `CURR` IS EVEN, ADD IT TO THE END OF THE EVEN CHAIN.
// * IF `CURR` IS ODD, ADD IT TO THE END OF THE ODD CHAIN.
// * `HEAD` POINTERS REMAIN FIXED AND REMEMBER THE START OF EACH CHAIN.
// * `TAIL` POINTERS MOVE FORWARD AND HELP APPEND NEW NODES.
// * AFTER TRAVERSING THE ENTIRE LIST, CONNECT `EVENTAIL` TO `ODDHEAD`.
// * RETURN `EVENHEAD` AS THE NEW HEAD.
// * WE DO **NOT CREATE NEW NODES OR NEW LINKED LISTS**; WE REARRANGE THE `NEXT` POINTERS OF THE EXISTING NODES.
// * THIS APPROACH PRESERVES THE ORIGINAL ORDER OF BOTH EVEN AND ODD NODES.
// * **TIME COMPLEXITY: O(N)**
// * **SPACE COMPLEXITY: O(1)**


class Solution {
public:
    Node* divide(Node* head) {
        if (head == nullptr || head->next == nullptr)
            return head;
        Node* evenHead = nullptr;
        Node* evenTail = nullptr;
        Node* oddHead = nullptr;
        Node* oddTail = nullptr;
        Node* curr = head;
        while (curr != nullptr) {
            Node* nextNode = curr->next;
            curr->next = nullptr;
            if (curr->data % 2 == 0) {
                if (evenHead == nullptr) {
                    evenHead = curr;
                    evenTail = curr;
                }
                else {
                    evenTail->next = curr;
                    evenTail = curr;
                }
            }
            else {
                // First odd node
                if (oddHead == nullptr) {
                    oddHead = curr;
                    oddTail = curr;
                }
                else {
                    oddTail->next = curr;
                    oddTail = curr;
                }
            }

            curr = nextNode;
        }

        if (evenHead == nullptr)
            return oddHead;
        // Connect even list to odd list
        evenTail->next = oddHead;
        return evenHead;
    }
};