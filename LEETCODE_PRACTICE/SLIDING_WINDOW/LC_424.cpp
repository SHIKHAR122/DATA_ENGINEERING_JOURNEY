// LEETCODE PROBLEM NUMBER 424 - LONGEST REPEATING CHARACTER REPLACEMENT 

#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public:
            int characterReplacement(string s, int k) { 
        //Step-1: Intialize variables and data structures
        int n = s.length();
        int left = 0;
        int maxLength = 0;//to store the output
        int maxFreq = 0;//to store the freq of curr char
        vector<int> freq(26, 0); //frequency array to check how many times occured
        //Step-2: Expand the sliding window
        for(int right = 0; right < n; right++){
            //Step-3: Update the freq of current char
            freq[s[right] - 'A']++;
            //Step-4: Update maximum frequency of a character
            maxFreq = max(maxFreq, freq[s[right] - 'A']);
            //Step-5: Shrink the window if replacement exceeds k
            while((right - left + 1) - maxFreq > k){
                
                freq[s[left] - 'A']--; //decrease freq of leftmost char
                left++;//move left pointer to shrink the size of window
            }
            //Step-6: Update maxLength
            maxLength = max(maxLength, right - left + 1);
        }
        //Step-7: Finally return the output
        return maxLength;
    }
};

int main()
{
    string s;
    cin>>s;
    int k;
    cin>>k;
    Solution sol;
    cout<<sol.characterReplacement(s,k);  
}