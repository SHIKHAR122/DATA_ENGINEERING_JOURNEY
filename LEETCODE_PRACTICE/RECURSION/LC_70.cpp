// LEETCODE PROBLEM NUMBER 70 - CLIMBING STAIRS

// FOR SOLVING THIS PROBLEM WE HAVE TO USE THE RECURSIVE APPROACH , WHERE THE MAIN FORMULA TO USE IF :
// STAIRS(n)  =   STAIRS(n-1) + STAIRS(n-2)

// WHERE THE BASE CASES WILL BE  -   1) WHEN THE NUMBER OF STAIRS IS 2 THEN OBVIOUSLY THE TOTAL COMBINATION WILL ALSO BE 2 
//                                   2)  WHEN THE NUMBER OF STAIRS IF 1 THEN THE TOTAL COMBINATION WILL BE ALSO 1 



// THE TIME COMPLEXITY TO SOLVE THIS QUESTION WILL BE O(n) STACK FRAMES AND  SPACE WILL BE(1) 


#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
        int NumberOfStairs(int n)
        {
            if(n==1) return 1;
            if(n==2) return 2;
            int ans=NumberOfStairs(n-1)+NumberOfStairs(n-2);
            return ans;
        }
};
int main()
{
    Solution sol;
    int res=sol.NumberOfStairs(4);
    cout<<res<<endl;
}