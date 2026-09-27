// LEETCODE PROBLEM NUMBER 39 - COMBINATION SUM - 
// THIS PROBLEM WILL BE SOLVED USING THE RECURSIVE APPROACH , WHERE WE ARE CALLING 2 TIMES - FIRST TIME THE NUMBER IS BEEN INCLUDED AGAIN FOR THE SUM AND 
// THE OTHER TIME IT IS NOT BEEN INCLUDED
// THE BASE CASE OF THIS PROBLEM WILL BE - IF THE TARGET IS MATCHED WITH THE SUM THEN PUSH THE COMBINATION ARRAY IN THE 2D ARRAY AND OTHER WISE 
// IF THE TOTAL>TARGET OR THE INDEX BECOMES GREATER THAN EQUAL TO THE CANDIDATES.SIZE() , THEN WE WILL SIMPLY RETURN 


class Solution {
public:
    void func(vector<int>&candidates,int target,int index , vector<vector<int>>&res,int total,vector<int>&combo)
    {
        if(total==target)
        {
            res.push_back(combo);
            return;
        }
        if(total>target||index>=candidates.size())
        {
            return;
        }
        combo.push_back(candidates[index]);
        func(candidates,target,index,res,total+candidates[index],combo);
        combo.pop_back();
        func(candidates,target,index+1,res,total,combo);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>>res;
        vector<int>combo;
        func(candidates,target,0,res,0,combo);
        return res;
    }
};