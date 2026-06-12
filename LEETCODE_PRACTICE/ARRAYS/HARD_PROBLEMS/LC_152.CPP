// LEETCODE PROBELM NUMBER 152 MAXIMUM SUBARRAY PRODUCT 

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int min_p=nums[0];
        int max_p=nums[0];
        int ans=nums[0];
        for(int i=1;i<nums.size();i++)
        {
            int curr=nums[i];
            if(curr<0)
            {
                swap(min_p,max_p);
            }
            max_p=max(curr,max_p*curr);
            min_p=min(curr,min_p*curr);
            ans=max(ans,max_p);
        }
               return ans;

    }
};