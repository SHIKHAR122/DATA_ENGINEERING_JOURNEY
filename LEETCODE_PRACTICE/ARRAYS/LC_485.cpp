//LEETCODE PROBLEM NUMBER 485 - MAX CONSECUTIVE ONES 
// TAKE TWO VARIABLES ONE TO STORE THE NUMBERS OF 1 AND ONE TO STORE THE MAX NUMBER OF 1s THAT OCCURED WHILE TRAVERSING ...
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_one=0;
        int count_one=0;
        for(int i=0;i<nums.size();i++)
        {   
            if(nums[i]==1)
            {
                count_one++;
            }
            else{
                count_one=0;
            }
            max_one=max(max_one,count_one);
        }
        return max_one;
    }
};