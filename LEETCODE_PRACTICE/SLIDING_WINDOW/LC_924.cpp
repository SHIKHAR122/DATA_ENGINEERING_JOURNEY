// LEETCODE PROBLEM NUMBER 924 - BINARY SUBARRAYS WITH SUM 


#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public: 
         int atmost(vector<int>&nums,int k )
    {
        if(k<0)return 0;
        int n=nums.size();
        int left=0;
        int count=0;
        int sum=0;
        for(int right=0;right<n;right++)
        {
            sum+=nums[right];
            while(sum>k)
            {
                sum-=nums[left];
                left++;
            }

            count=count+(right-left+1);
        }
        return count;
    }
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        return atmost(nums,goal)-atmost(nums,goal-1);
    }
    

};
int main()
{
        Solution sol;
        vector<int>nums;
        int goal;
        sol.numSubarraysWithSum(nums  , goal);
}