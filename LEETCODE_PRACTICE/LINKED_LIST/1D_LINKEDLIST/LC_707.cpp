// LEETCODE PROBLEM NUMBER 707 DESIGN A LINKED LIST 



#include<iostream>
#include<algorithm>
using namespace std

class MyLinkedList {
public:
    struct Node
    {
        int data;
        Node* next;
        Node(int val)
        {
            data=val;
            next=NULL;
        }

    };
    Node* head;
    MyLinkedList() {
        head=NULL;
    }
    int getLength(Node* head)
    {
        int count=0;
        Node* temp=head;
        while(temp!=NULL)
        {
            count++;
            temp=temp->next;
        }
        return count;
    }
    int get(int index) {
        int count=0;
        Node*temp=head;
        while(temp!=NULL)
        {
            
            if(count==index)
            {
                return temp->data;
            }
            temp=temp->next;
            count++;
        }   
        return -1;
    }
    
    void addAtHead(int val) {
        Node* newNode= new Node(val);
        newNode->next=head;
        head=newNode;        
    }
    
    void addAtTail(int val) {
        if(head==NULL)
        {
            head= new Node(val);
            return ;
        }
        Node*curr=head;
        while(curr->next!=NULL)
        {
            curr=curr->next;
        }
        Node*newNode=new Node(val);
        curr->next=newNode;
    }
    
    void addAtIndex(int index, int val) {
        if(index==0)
        {
            Node*temp=new Node(val);
            temp->next=head;
            head=temp;
            return;
        }
        if(index==getLength(head))
        {
            Node* temp= head;
            while(temp->next!=NULL)
            {
                temp=temp->next;
            }
            Node* newNode= new Node(val);
            newNode->next=temp->next;
            temp->next=newNode;
            return ; 
        }
        Node*temp=head;
        int count=0;
        
        while(temp!=NULL)
        {
            if(count==index-1)
            {
            Node*newNode= new Node(val);
            newNode->next=temp->next;
            temp->next=newNode;
            break;
            }
            count++;
            temp=temp->next;
        }
       


    }
    
    void deleteAtIndex(int index) {
        if(head==NULL) return ;
        if(index==0)
        {
            Node*temp=head;
            head=head->next;
            delete temp;
            return ;
        }
        int count=0;
        Node* temp=head;
        Node* prev=NULL;
        while(temp!=NULL)
        {
            if(count==index)
            {
                prev->next=temp->next;
                delete temp;
                return;
            }
            count++;
            prev=temp;
            temp=temp->next;
        }
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */