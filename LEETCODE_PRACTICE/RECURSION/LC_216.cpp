// LEETCODE PROBLEM NUMBER 216 - COMBINATION SUM III

// THIS QUESTION CAN BE SOLVED SIMPLY BY COMBINING THE LOGIC OF THE PREVIOUS TWO VARIANTS OF THIS QUESTION THAT IS THE COMBINATION SUM I & II


#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:

    void func(vector<int>& candidates,vector<vector<int>>& res, vector<int>& combo,int target,int index,int total,int count,int k)
    {
        if(count == k)
        {
            if(target == total)
            {
                res.push_back(combo);
            }

            return;
        }
        if(total > target || index >= candidates.size())
        {
            return;
        }
        // TAKE
        combo.push_back(candidates[index]);
        func(candidates,res,combo,target,index + 1,total + candidates[index],count + 1,k);
        combo.pop_back();
        // DON'T TAKE
        func(candidates,res,combo,target, index + 1,total, count,k);
    }
};
int main()
{
    Solution sol;
    vector<int> candidates = {1,2,3,4,5,6,7,8,9};
    int target = 7;
    int index = 0;
    vector<vector<int>> res;
    int total = 0;
    vector<int> combo;
    int count = 0;
    int k = 3;
    sol.func(candidates, res, combo,target, index, total, count, k);

    for(auto x : res)
    {
        for(auto y : x)
        {
            cout << y << " ";
        }
        cout << endl;
    }
}