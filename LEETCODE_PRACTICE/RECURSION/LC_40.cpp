// LEETCODE PROBLEM NUMBER 40 - COMBINATION SUM II 

// THIS PROBLEM HAS THE SAME APPROACH AS THAT OF LC - 39 , THE ONLY DIFFERENCE IS THAT WE WILL BE USING A BOOLEAN FLAG TO MARK THE ELEMENTS WHICH 
// HAVE BEEN USED IN MAKING THE COMBINATION FIRST i.e., THERE SHOULD BE A FLAG THAT ENSURES THAT THE ELEMENT TO BE PUSHED AND THE ELEMENT WHICH IS
// CURRENTLY IN THE RESULTANT VECTOR ARE SAME OR NOT , IF THE FLAG IS TRUE IT MEANS THE ELEMENTS BOTH IN THE ORIGINAL VECTOR AND THE RESULTANT VECTOR
// HAVE THE SAME VALUE AND VICE VERSA



class Solution {
public:

    void func(vector<int>& candidates, int target, int idx, int total,
              vector<int>& combo, vector<vector<int>>& res, bool flag)
    {
        if(total == target)
        {
            res.push_back(combo);
            return;
        }
        if(total > target || idx >= candidates.size())
        {
            return;
        }
        if(flag == true)
        {
            combo.push_back(candidates[idx]);
            func(candidates,target, idx + 1,total + candidates[idx],combo,res,true);
            combo.pop_back();
        }
        if(idx + 1 < candidates.size() &&
           candidates[idx] == candidates[idx + 1])
        {
            func(candidates, target,idx + 1, total,combo, res , false);
        }
        else
        {
            func(candidates,target,idx + 1, total, combo,res,true);
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target)
    {
        vector<vector<int>> res;
        vector<int> combo;
        sort(candidates.begin(), candidates.end());
        func(candidates, target, 0, 0, combo, res, true);
        return res;
    }
};