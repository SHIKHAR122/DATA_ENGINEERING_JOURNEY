// LEETCODE PROBLEM NUMBER 3 - LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS 

#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i=0;  //this is the i th pointer -> left side of the window
        int j=0;    // this is the jth pointer -> right side of the window 
        int n=s.size(); 
        int len=0;  //for storing the current length of the string
        int maxlen=0;  //for storing the maximum length of the string obtained
        unordered_map<char,int>mp;
        while(j<n)
        {
            mp[s[j]]++; //if the current element is not found/seen in the map then simply keep incrementing its freq. (which will always be 1 as we are storing the unique elements)
            while(mp[s[j]]>1) // if the freq of the current element is more than 1 it means that we have seen this in the map before 
            {
                mp[s[i]]--;  //so simply reduce the freq of that element till when we have reached a point where the freq is 0 or 1 
                i++;
            }
             len=j-i+1;
             maxlen=max(maxlen , len); 
             j++;  
        }
        return maxlen;
    }
};

int main()
{
    Solution sol;
    string s;
    cin>>s;
   cout<< sol.lengthOfLongestSubstring(s);
}