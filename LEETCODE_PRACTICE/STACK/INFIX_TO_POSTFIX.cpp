#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public:
           int solve(int val1 , int val2 , int opr)
           {
                if(opr=='+')
                {
                    return val1+val2;
                }
                else if (opr=='-')
                {
                    return val1-val2;
                }
                else if (opr=='*')
                {
                    return val1*val2;
                }
                else 
                {
                    return val1/val2;
                }
              
           }
           int InfixToPostfix(string s)
           {
                stack<int>val;
               
                int n=s.length();
                for(int i=0;i<n;i++)
                {
                    if(s[i]>=48 && s[i]<=58)
                    {
                        val.push(s[i]-48);
                    }
                    else 
                    {
                        int val2=val.top();
                        val.pop();
                        int val1=val.top();
                        val.pop();
                        int ans=solve(val1,val2,s[i]);
                        val.push(ans);
                    }
                }
                
           }

};
int main ()
{
    string s ;
    cout<<"ENTER THE INFIX EXPRESSION : ";
    cin>>s; 
    Solution sol;
    string result=sol.InfixToPostfix(s);
}