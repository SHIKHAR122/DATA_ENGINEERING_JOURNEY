// LEETCODE PROBLEM NUMBER 81 - SEARCH IN ROTATED ARRAY - II

// THIS PROBLEM IS SAME AS THE PREVIOUS ONE THAT IS THE SEARCH IN ROTATED ARRAY -I , THE ONLY LOGIC ADDED IS 
// IS TO SIMPLY MOVE THE LOW AND HIGH POINTERS ON FINDING A MATCHING TERM 


class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int n=nums.size();
        int low=0;
        int high=n-1;
        while(low<=high)
        {
            int mid = low + (high-low)/2;
            if(nums[mid]==target)
            return true;
            if(nums[low]==nums[mid]&& nums[high]==nums[mid])
            {  
                low++;
                high--;
                continue;
            } 
            if(nums[low]<=nums[mid])
            {
                if(nums[low]<=target && target<nums[mid])
                {   
                    high=mid-1;
                }
                else{
                    low=mid+1;
                }
            }
            else if(nums[mid]<target && target<=nums[high])
            {
                low=mid+1;
            }
            else {
                high=mid-1;
            }
        }
        return false;
    }
};