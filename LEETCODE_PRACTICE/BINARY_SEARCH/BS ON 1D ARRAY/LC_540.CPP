// LEETCODE PROBLEM NUMBER 540 - SINGLE ELEMENT IN THE SORTED ARRAY .

class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int low=0;
        int high=nums.size()-1;
        while(low<high)
        {
            int mid= low + (high-low)/2;
            if((mid%2==0 && nums[mid]==nums[mid+1])||(mid%2==1 && nums[mid]==nums[mid-1]))
            {
                low=mid+1;
            }
            else {
                high=mid;
            }
        }
        return nums[low];
    }
};