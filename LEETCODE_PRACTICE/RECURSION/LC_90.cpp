//LEETCODE PROBLEM NUMBER 90 - SUBSETS II
class Solution {
public:
    void subsets(vector<int>& nums, vector<vector<int>>& ans, vector<int>& current,int index,bool flag)
    {
        if(index == nums.size())
        {
            ans.push_back(current);
            return;
        }
        if(index == nums.size() - 1)
        {
            current.push_back(nums[index]);
            if(flag == true)
                subsets(nums, ans, current, index + 1, true);
            current.pop_back();
            subsets(nums, ans, current, index + 1, true);
            return;
        }
        int first = nums[index];
        int second = nums[index + 1];
        if(first == second)
        {
            current.push_back(nums[index]);
            if(flag == true)
                subsets(nums, ans, current, index + 1, true);
            current.pop_back();
            subsets(nums, ans, current, index + 1, false);
        }
        else
        {
            current.push_back(nums[index]);
            if(flag == true)
                subsets(nums, ans, current, index + 1, true);
            current.pop_back();
            subsets(nums, ans, current, index + 1, true);
        }
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums)
    {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        vector<int> current;
        subsets(nums, ans, current, 0, true);
        return ans;
    }
};