// LEETCODE PROBLEM NUMBER 78 - SUBSETS 


class Solution {
public:
    void fun(vector<vector<int>>&ans , vector<int>&nums , vector<int>current , int index)
    {
        if(index==nums.size())
        {
            ans.push_back(current);
            return;
        }
        current.push_back(nums[index]);
        fun(ans , nums , current , index+1); //case 1 when we have to push
        current.pop_back();
        fun(ans , nums , current , index+1); // case 2 when we dont have to push
    }   
    vector<vector<int>> subsets(vector<int>& nums) {    
        vector<vector<int>>ans ;
        vector<int>current ;
        fun(ans , nums , current , 0);
        return ans;
    }
};