// LEETCODE PROBLEM NUMBER 33 - SEARCH IN A SORTED AND ROTATED ARRAY 
// IN THIS PROBLEM WE ARE CHECKING 2 CONDITIONS EVERYTIME , 1 IS CHECK WHICH HALF OF THE ARRAY I.E., LEFT OR THE RIGHT SIDE OF THE ARRAY
//IS SORTED AND THEN 2  CHECK IF THE TARGET IS PRESENT IN THAT HALF OR NOT IF PRESENT THEN RETURN IT OTHER WISE SEARCH IN THE
//OTHER HALF OF THE ARRAY


class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low=0;
        int high=nums.size()-1;
        while(low<=high) {
            int mid= low + (high-low)/2;
            if(nums[mid]==target)
                return mid;
            if(nums[low]<=nums[mid]) {
                if(nums[low]<=target && target<nums[mid]) {
                    high=mid-1;
                }
                else {
                    low=mid+1;
                }
            }
            else {
                if(nums[mid]<target && target<=nums[high]) {
                    low=mid+1;
                }
                else {
                    high=mid-1;
                }
            }
        }
        return -1;
    }
};