// GFG PROBLEM - LONGEST SUBSTRING WITH ATMOST 'K' DISTINCT CHARACTERS 
//THIS IS THE CLASSIC VARIABLE SIZE WINDOW PATTERN OF THE SLIDING WINDOW 
//HERE WE  WILL SIMPLY USE THE HASHMAP TO STORE THE FREQUENCY OF THE ELEMENTS AT THE RIGHT
// WHEN THE MAP SIZE BECOMES GREATER THAN THE GIVEN VALUE OF 'K' WE WILL SIMPLY DECREASE THE FREQUENCY OF THE LEFT MOST ELEMENT FROM THE MAP 
// AND KEEP THR TRACK OF THE SIZE AND AS SOON AS THE SIZE OF THE MAP IS EQUAL TO THE SIZE OF K GIVEN , WE GET TO KNOW THAT THE MAP IS HAVINIG K DISTICT ELEMENTS 
//  SO SIMPLY UPDATE THE SIZE OF THE MAX LENGTH


#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public:
          int longestKSubstr(string &s, int k) {
        // code here
        int left=0;  
        int right=0;
        int n=s.size();
        int len=0;
        int maxlen=INT_MIN;
        unordered_map<char,int>mp;
        while(right<n)
        {
            mp[s[right]]++;
            while(mp.size()>k)
            {   
                mp[s[left]]--;
                if(mp[s[left]]==0)
                {
                    mp.erase(s[left]);
                }
                left++;
            }
            len=right-left+1;
            if(mp.size()==k)  //if the size of the map is equal to the size of the k that means we have got the potentiol disctinct elementts in the map so update the map
            
            {
                maxlen=max(maxlen , len);
            }
            right++;
        }
        if(maxlen==INT_MIN) return -1;
        return maxlen;
    }
};
int main()
{
    string s;
    cout<<"ENTER THE STRING ELEMENT :";
    cin>>s;
    int k;
    cout<<"ENTER THE SIZE OF 'K': ";
    cin>>k;
    Solution sol;
    int result =sol.longestKSubstr(s , k);
    cout<<result;
}