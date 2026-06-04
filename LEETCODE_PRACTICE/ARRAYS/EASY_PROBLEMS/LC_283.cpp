// LEETCODE PROBLEM NUMBER 283 - MOVE ZEROES TO THE END 
//SOLVED UISNG THE SINGLE TRAVERSAL METHOD 
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i=0;
        int n=nums.size();
        for(int j=1;j<n;j++)
        {
            if(nums[j]!=0)
            {
                swap(nums[i],nums[j]);
                i++;
            }
        }
    }
};