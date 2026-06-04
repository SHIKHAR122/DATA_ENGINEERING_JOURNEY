//LEETCODE PROBLEM NUMBER 1752 -  CHECK IF ARRAY IS SORTED OR NOT 
//CHECK THE BREAK POINT OF THE ARRAY , USING CIRCULAR TECHNIQUE , IF BREAKPOINT = 1 THEN IT IS A VALID ARRAY OTHERWISE NOT VALID ...
class Solution {
public:
    bool check(vector<int>& nums) {
        int count=0;
        int n=nums.size();
        for(int i=0;i<n;i++)
        {   
            if(nums[i]>nums[(i+1)%n])
            {
                count++;
            }
        }
            return count<=1;
    }
};