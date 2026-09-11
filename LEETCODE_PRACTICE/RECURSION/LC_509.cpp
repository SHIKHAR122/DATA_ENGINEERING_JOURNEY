// LEETCODE PROBLEM NUMBER 509 - FIBONACCI NUMBERS 


// THIS FOLLOWING PROBLEM CAN BE SOLVED USING THE RECURSIVE APPROACH WHERE THE BASE CASES ARE  -
//  1) IF N==1 RETURN 1 AND 2) IF N==0 RETURN 0


class Solution {
public:
    int fib(int n) {
        if(n==0) return 0;
        if(n==1) return 1;
        int ans= fib(n-1)+fib(n-2);
        return ans;
    }
};