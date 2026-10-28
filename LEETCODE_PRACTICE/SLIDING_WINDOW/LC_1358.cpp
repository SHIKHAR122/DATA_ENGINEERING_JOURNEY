// LEETCODE PROBLEM NUMBER 1358 - NUMBER OF SUBSTRING CONTAINING ALL THREE CHARACTERS


#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public:
        int numberOfSubstrings(string s) {
            int left = 0;
            int ans = 0;
            int right=0;
            int n=s.size();
            unordered_map<char, int> mp;
            while(right<n)
            {
                mp[s[right]]++;
                while(mp['a']>0 && mp['b']>0 && mp['c']>0)
                {
                    mp[s[left]]--;
                    left++;
                }
                ans+=left;
                right++;
            }
            return ans;
        }
};
int main()
{
    string s;
    cout<<"ENTER THE STRING: ";
    cin>>s;
    Solution sol;
    cout<<sol.numberOfSubstrings(s); 
}