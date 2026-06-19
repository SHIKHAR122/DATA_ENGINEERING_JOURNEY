// LEETCODE PROBLEM NUMBER 162 - FIND PEAK ELEMENTS 


// THIS QUESTION CAN BE SOLVED USING TWO LOGICS 


// NUMBER 1 LOGIC - WHERE WE HAVE TO HANDLE SOME OF THE TEST CASES - 
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();

        if(n == 1) return 0;

        if(nums[0] > nums[1]) return 0;
        if(nums[n-1] > nums[n-2]) return n-1;

        int low = 1;
        int high = n - 2;

        while(low <= high) {
            int mid = low + (high - low) / 2;

            if(nums[mid] > nums[mid-1] && nums[mid] > nums[mid+1]) {
                return mid;
            }
            else if(nums[mid] < nums[mid+1]) {
                low = mid + 1;
            }
            else {
                high = mid - 1;
            }
        }

        return -1;
    }
};




//   LOGIC - 2 WHICH IS MORE OPTIMAL 
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
        int low=0;
        int high=n-1;
        while(low<high)
        {
            int mid = low + (high-low)/2;
            if(nums[mid]>nums[mid+1]){
                high = mid;
            }
            else 
            {
                low=mid+1;
            }
              
        }
        return low ;
    }
};