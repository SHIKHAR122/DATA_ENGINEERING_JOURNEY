// GFG QUESTION 2  - PARANTHESIS CHECKER 


// Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. Determine whether the Expression is balanced or not.
// An expression is balanced if:

// Each opening bracket has a corresponding closing bracket of the same type.
// Opening brackets must be closed in the correct order.


#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public:
           bool IsValid(string &s)
           {
                stack<char>st;
                for(char ch : s )
                {
                    if(ch=='{'||ch=='['||ch=='(')
                    {
                        st.push(ch);
                    }
                    else 
                    {
                        if(st.empty())
                        {
                            return false;
                        }
                        if((ch == ')' && st.top() != '(') ||
                    (
                        ch == ']' && st.top() != '[') ||
                    (ch == '}' && st.top() != '{')) {
                        return false;
                    }
                        st.pop();
                    }
                }
                    return st.empty();
                }    
        };

int main()
{
    string s ;
    cout<<"ENTER THE STRING : ";
    cin>>s;
    Solution sol;
    cout<<sol.IsValid(s); 
}