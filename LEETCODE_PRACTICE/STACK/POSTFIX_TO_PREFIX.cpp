// THIS IS THE IMPLEMENTATITON OF POSTFIX EXPRESSION TO PREFIX EXPRESSION 

#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public:
            string solve(string val1 , string val2 , char opr)
            {
                    string s="";
                    s.push_back(opr);
                    s+=val1;
                    s+=val2;
                    return s;
            }
           string PostToPrefix(string s)
           {
                stack<string>val;
                for(int i=0;i<s.length();i++)
                {
                    if(s[i]>=48 && s[i]<=57)
                    {
                        val.push(to_string(s[i]-48));
                    }
                    else
                    {
                        string val2=val.top();
                        val.pop();
                        string val1=val.top();
                        val.pop();
                        string ans = solve(val1 ,val2 ,s[i]);
                        val.push(ans);
                    }
                }
           }
};
int main ()
{
    string s ;
    cout<<"ENTER THE POSTFIX EXPRESSION : ";
    cin>>s;
    Solution sol;
    string result = sol.PostToPrefix(s);
    cout<<result;
}