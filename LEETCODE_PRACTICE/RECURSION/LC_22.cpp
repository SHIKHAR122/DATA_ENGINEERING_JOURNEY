// // LEETCODE PROBLEM NUMBER 22 - GENERATE PARANTHESES - 

// > **Approach:** Use recursion/backtracking with `open` and `close` counters to generate all valid parentheses combinations.
// >
// > * If `open == n`, only `)` can be added.
// > * If `open == close`, only `(` can be added to avoid an invalid sequence.
// > * If `open > close`, both `(` and `)` can be added, creating two recursive branches.
// > * When `open == close == n`, the complete valid string is added to the result.

// **Pattern:** `Backtracking + Recursion + Constraint-based branching`
// **Time:** `O(4^n / √n)` combinations generated
// **Extra recursion space:** `O(n)` (excluding output).


class Solution {
public:
    void perm(string ans , vector<string>&res , int open , int close , int n)
    {
        if(open==n&&close==n)
        {
            res.push_back(ans);
            return ;
        }
        if(open==n)
        {
            perm(ans+")" , res , open ,close+1 , n);
        }
        else if (close==open)
        {
            perm(ans+"(",res ,open+1 ,close ,n);
        }
        else if(open>close&&open<n)
        {
            perm(ans+"(" , res , open+1 , close ,n);
            perm(ans+")" , res, open  , close+1 ,n);
        }
    }
    vector<string> generateParenthesis(int n) {
         vector<string>res;
         perm("",res,0,0,n);
         return res;
    }
};