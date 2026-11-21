#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public:
           int priority(char value)
           {
                if(value=='+'||value=='-') 
                {
                    return 1;
                }
                else return 2;
           }

           string solve(string val1 , string val2 , char opr)
           {    
                string s="";
                s.push_back(opr);
                s+=val1;
                s+=val2;
                return s ; 
           }

           string InfixToPrefix(string s)
           {
                stack<string>val;
                stack<char>opr;
                for(int i=0;i<s.size();i++)
                {       
                    if(s[i]>=48 && s[i]<=57)
                    {
                        val.push(to_string(s[i]-48));
                    }
                    else 
                    {
                        if(opr.empty())
                        {
                            opr.push(s[i]);
                        }
                        else if (s[i]=='(')
                        {
                            opr.push(s[i]);
                        }
                        else if(opr.top()=='(')
                        {
                            opr.push(s[i]);
                        }
                        else if (s[i]==')')
                        {
                            while(!opr.empty() && opr.top()!='(')
                            {
                                char ch=opr.top();
                                opr.pop();
                                string val2=val.top();
                                val.pop();
                                string val1=val.top();
                                val.pop();
                                string ans=solve(val1,val2,ch);
                                val.push(ans);
                            }
                            opr.pop();
                        }
                        else if(priority(s[i])>priority(opr.top()))
                        {
                            opr.push(s[i]);
                        }
                        else 
                        {
                            while(!opr.empty() && opr.top()!='(' && priority(s[i])<=priority(opr.top()))
                            {
                                char ch=opr.top();
                                opr.pop();
                                string val2=val.top();
                                val.pop();
                                string val1=val.top();
                                val.pop();
                                string ans=solve(val1,val2,ch);
                                val.push(ans);
                            }
                            opr.push(s[i]);
                        }                        
                    }
                }
                while(!opr.empty())
                {
                    char ch = opr.top();
                    opr.pop();
                    string val2=val.top();
                    val.pop();
                    string val1=val.top();
                    val.pop();
                    string ans=solve(val1,val2,ch);
                    val.push(ans);
                }
                return val.top();
           } 
};

int main ()
{
    Solution sol;
    string s;
    cout<<"ENTER THE INFIX EXPRESSION : "<<endl;
    cin>>s;
    string result=sol.InfixToPrefix(s);
    cout<<"******RESULT*******"<<endl;
    cout<<result<<endl;
    return 0;
}