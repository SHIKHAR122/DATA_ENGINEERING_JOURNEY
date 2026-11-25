// HERE WE HAVE IMPLEMENTED THE PREFIX EXPRESSION IMPLEMENTATION 
#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public:
           int solve(int val1 , int val2 , char opr)
           {
                if(opr=='-') return val1-val2;
                else if (opr=='+') return val1+val2;
                else if (opr=='*') return val1*val2;
                else return val1/val2;
           }

           int PrefixEval(string s)
           {
             stack<int>val;
             int n=s.length();
             for(int i=n-1;i>=0;i--)
             {
                if(s[i]>=48 && s[i]<=57)
                {   
                    val.push(s[i]-48);
                }
                else {
                    int val1=val.top();
                    val.pop();
                    int val2=val.top();
                    val.pop();
                    int ans=solve(val1 , val2 , s[i]);
                    val.push(ans);
                }
             }
                return val.top();
           }
};


int main()
{
    Solution sol;
    string s; 
    cout<<"ENTER THE PREFIX EXPRESSION : ";
    cin>>s;
    int  result=sol.PrefixEval(s);
    cout<<result<<endl;
}