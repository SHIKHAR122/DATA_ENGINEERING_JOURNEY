// LEETCODE PROBLEM NUMBER 34 - FIND THE FIRST AND THE LAST POSITION OF ELEMENTS IN THE SORTED ARRAY
// WE WILL SOLVE THIS PROBLEM BY USING THE BINARY SEARCH 2 TIMES - ONE FOR THE FIRST OCCURENCE(LEFT) AND THE OTHER FOR THE LAST (RIGHT)



class Solution {
public:
    int first_occurence(vector<int>& nums, int target)
    {
        int first=-1;
        int low=0;
        int high= nums.size()-1;
        while(low<=high)
        {   
            int mid= low+(high-low)/2;
            if(nums[mid]==target)
            {   
                first=mid;
                high=mid-1;
            }
            else if(nums[mid]<target){
             
                low=mid+1;
            }
            else
            {
                high=mid-1;
            }
        }
        return first;
    }
    int last_occurence(vector<int>& nums, int target)
    {
        int end=-1;
        int low=0;
        int high=nums.size()-1;
        while(low<=high)
        {
            int mid= low + (high-low)/2;
            if(nums[mid]==target)
            {
                end=mid;
                low=mid+1;
            }
            else if (nums[mid]>target)
            {
                high=mid-1;
            }
            else {
                low=mid+1;
            }
        }
        return end;
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        int first = first_occurence(nums, target);
        if(first == -1)
        return {-1, -1};
        int last = last_occurence(nums, target);
        return {first , last};
    }
};