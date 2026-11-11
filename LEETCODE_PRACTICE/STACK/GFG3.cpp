// GFG QUESTION NUMBER 3- REPLACE CONSECUTIVE TWO SAME WITH ONES

// Given a string s, consisting of lowercase alphabets. Remove consecutive duplicate characters from the string. 


#include<bits/stdc++.h>
using namespace std;
class Solution {
    public:
        string removeDuplicates(string& s) {
        stack<char>st;
        string res="";
        for(char ch : s)
        {
            if(st.empty() || st.top()!=ch)
            {
                st.push(ch);
            }
        }
        while(!st.empty())
        {
            res+=st.top();
            st.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
};


int main()
{
    string s;
    cout<<"ENTER THE STRING ELEMENTS ";
    cin>>s;
    Solution sol;
    cout<<sol.removeDuplicates(s);
}


