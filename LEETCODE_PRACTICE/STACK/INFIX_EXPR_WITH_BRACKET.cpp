#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public:
          int priority(char value)
          {
            int p;
             if(value=='+'||value=='-')  //if the operator is addiotion or subtraction then we will return 1 as the priority 
             {
                 p=1;
             }
             else {  //else if the operator is '*' or "/" , then we return 2 as the priority
                p=2;
             }
             return p;
          }
          int solve(int value1 , int value2, char opr)
          {
            if(opr=='+')   //if the operator is + then we will return the sum
            {
                return value1+value2;
            }
            else if (opr=='-')  //if the operator is - then we will return the difference between the value 1 and value 2
            {
                return value1-value2;
            }
            else if(opr=='/') //if the operator is / then we will send the quotient as the result 
            {
                return value1/value2;
            }
            else  //if its a * sign then we will return the product of the two numbers 
            {
                return value1*value2;
            }
          }
          int InfixExpression(string s )
          {
              stack<int>value ; // this stack will be used to store the numeric value of the expresssion
              stack<char>opr; //this stack will be used to store the operators in the stack 
              int n=s.length();
              
              for(int i=0;i<n;i++)  //using this for loop we will simply move traverse the whole expression to check if its a operator or a number 
              {         
                //check if s[i] is a digit or a character 
                int ascii= (int)(s[i]);
                 if(ascii>=48 && ascii<=57)   //this is the range of the ascii values of the numbers (integers from 0-9)
                 {
                    value.push(s[i]-48);
                 }
                 else {
                     if(opr.empty())  //if the operator stack is empty then we can push the operator without any issues 
                     {
                        opr.push(s[i]);
                     }
                    else if(s[i]=='(')  //if s[i] is an opening bracket then we will simply push it to the stack
                     {
                        opr.push(s[i]);
                     }
                     else if(opr.top()=='(')  //if the top is also a top bracket then we will also push it
                     {
                        opr.push(s[i]);
                     }
                     else if(s[i]==')')
                     {
                         while(opr.top()!='(')  // we will keep solving until we get an opening bracket at the top of the stack
                         {
                            char ch = opr.top();   //getting the operator from the opr stack
                            opr.pop();  //popping the operator which is been used 
                            int val2=value.top(); //the value's stack top is the value 2
                            value.pop(); //pop the current value to get the first value 
                            int val1=value.top();
                            value.pop();
                            int ans =solve(val1,val2,ch);
                            value.push(ans);
                        }
                        opr.pop();  ///we are popping the opening bracket after solving the above logic
                     }
                     else if (priority(s[i])>priority(opr.top())) //also if the priority of the current operator is more than the priority of the stack top's then we will also push it again
                     {
                        opr.push(s[i]);
                     }  
                     else {  //but if both the conditions are false then we will simply solve the expression -> VAL 1 operator VAL 2
                        while(opr.size()>0 && priority(s[i])<=priority(opr.top()))  //we will keep performing the operation till the condition -> priority(s[i])<=priority(opr.top()) becomes false
                        {
                            char ch = opr.top();   //getting the operator from the opr stack
                            opr.pop();  //popping the operator which is been used 
                            int val2=value.top(); //the value's stack top is the value 2
                            value.pop(); //pop the current value to get the first value 
                            int val1=value.top();
                            value.pop();
                            int ans =solve(val1,val2,ch);
                            value.push(ans);
                        }
                        opr.push(s[i]);
                     }
                 }
              }

              //the operator stack can still have some values inside it so better make it empty
              while(!opr.empty())
              {
                    char ch = opr.top();   //getting the operator from the opr stack
                    opr.pop();  //popping the operator which is been used 
                    int val2=value.top(); //the value's stack top is the value 2
                    value.pop(); //pop the current value to get the first value 
                    int val1=value.top();
                    value.pop();
                    int ans =solve(val1,val2,ch);
                    value.push(ans);
              }
              return value.top();   //after all the operation , we can simply return the top element of the stack (value stack)
          }
};
int main()
{
    string s ;
    cout<<"ENTER AN INFIX EXPRESSION : ";
    cin>>s;
    Solution sol;
    int result= sol.InfixExpression(s);
    cout<<"*********RESULT*********"<<endl;
    cout<<result<<endl;
    return 0;
} 