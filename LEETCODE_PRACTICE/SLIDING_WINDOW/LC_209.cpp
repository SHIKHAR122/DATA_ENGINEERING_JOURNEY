// LEETCODE  PROBLEM NUMBER 209 - MINIMUM SIZE SUBARRAY SUM

#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
          int minSubArrayLen(int target, vector<int>& nums) {
          int n=nums.size();
          int i=0;
          int j=0;
          int len=0;
          int sum=0;
          int minlen=INT_MAX;
          while(j<n)
          {
             sum+=nums[j];
             while(sum>=target)
             {  
                len=j-i+1;
                minlen=min(minlen,len);
                sum-=nums[i];
                i++;
             }
             j++;
          } 
          if(minlen==INT_MAX) return 0;
          return minlen;
    }
};
int main()
{
    Solution sol;
    int target=10;
    vector<int>nums={1,2,4,6,3,4,3};
    cout<<sol.minSubArrayLen(target,nums);
}