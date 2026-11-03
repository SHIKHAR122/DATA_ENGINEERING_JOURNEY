// LEETCODE PROBLEM NUMBER 992 SUBARRAYS WITH K DIFFERENT INTEGERS
// THIS PROBLEM WILL BE SOLVED USING THE ATMOST() CONCEPT , WHICH WILL BE USED IN THE FOLLOWING METHOD :
// KEEP INCREASING THE FREQUENCY OF THE ELEMENT IN THE MAP WHICH IS POINTED BY THE RIGHT POINTER 
//  NOW CHECK IF THE SIZE OF THE MAP IS GREATER THAN 'K' , THAT MEANS THERE ARE MORE THAN K DISTINCT ELEMENTS IN THE MAP , WHICH WE DONT NEED 
// SO REMOVE THAT ELEMENT FROM THE LEFT MOST OF THE MAP
// THEN FINALLY COUNT THE NUMBER OF ELEMENTS BY THE FORMULA - count+=(right-left)+1
#include<bits/stdc++.h>
using namespace std;
class Solution {
    public:
              int atmost(vector<int>&nums , int k)
    {
        if(k<0) return 0;
        int n=nums.size();
        int left=0;
        int count=0;
        unordered_map<int ,int >mp;
        for(int right=0;right<n;right++)
        {
            mp[nums[right]]++;
            while(mp.size()>k)
            {
                mp[nums[left]]--;
                if(mp[nums[left]]==0)
                {
                    mp.erase(nums[left]);
                }
                left++;
            }
            count=count+(right-left+1);
        }
        return count;
    }
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        return atmost(nums , k)-atmost(nums , k-1);
    }
};
int main ()
{
    vector<int>nums;
    int k;
    Solution sol;
    cout<<sol.subarraysWithKDistinct(nums,k);
}