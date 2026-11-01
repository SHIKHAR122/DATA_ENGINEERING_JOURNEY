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
    sol.subarraysWithKDistinct(nums,k);

}