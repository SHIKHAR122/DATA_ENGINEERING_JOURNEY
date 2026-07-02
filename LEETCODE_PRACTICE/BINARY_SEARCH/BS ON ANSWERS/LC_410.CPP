// LEETCODE PROBLEM NUMBER 410 - SPLIT ARRAY LARGEST NUMBER
class Solution {
public:
    int countSubarrays(vector<int>& nums, int maxSum)
    {
        int subarrays = 1;
        int currentSum = 0;
        for(int num : nums)
        {
            if(currentSum + num > maxSum)
            {
                subarrays++;
                currentSum = num;
            }
            else
            {
                currentSum += num;
            }
        }

        return subarrays;
    }

    int splitArray(vector<int>& nums, int k) {
        int low = *max_element(nums.begin(), nums.end());
        int high = accumulate(nums.begin(), nums.end(), 0);
        while(low <= high)
        {
            int mid = low + (high - low) / 2;
            if(countSubarrays(nums, mid) <= k)
            {
                high = mid - 1;
            }
            else
            {
                low = mid + 1;
            }
        }
        return low;
    }
};