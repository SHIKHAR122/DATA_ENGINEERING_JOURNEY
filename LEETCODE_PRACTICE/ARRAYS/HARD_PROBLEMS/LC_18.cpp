//LEETCODE PROBLEM NUMBER 18 - FOURSUM
//THIS QUESTION HAS THE  SAME SOLUTION AS THAT OF THE 3SUM PROBLEM(LC-15)
//INSTEAD OF FIXING 1 VARIABLE , HERE WE WILL BE FIXING 2 VARIABLES..
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>>result;
        int n = nums.size();
        long long sum=0;
        sort(nums.begin(),nums.end());
        for(int i =0 ;i<n-3;i++)
        {
            if(i>0&&nums[i]==nums[i-1])
            {
                continue;
            }
            for(int j =i+1; j<n-2;j++)
            {   
                if(j>i+1&&nums[j]==nums[j-1])
                {
                    continue;
                }
                int left=j+1;
                int right=n-1;
                while(left<right)
                {
                    sum=(long long)nums[i]+nums[j]+nums[left]+nums[right];
                    if(sum<target)
                    {
                        left++;
                    }
                    else if(sum>target)
                    {
                        right--;
                    }
                    else
                    {
                        result.push_back({nums[i],nums[j],nums[left],nums[right]});
                        left++;
                        right--;
                    while(left<right&&nums[left]==nums[left-1])left++;
                    while(left<right&&nums[right]==nums[right+1])right--;
                    }
                }
            }
        }
        return result;
    }
};