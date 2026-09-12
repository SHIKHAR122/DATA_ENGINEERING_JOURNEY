// LEETCODE PROBLEM NUMBER 50 - POW(X,N)


// APPROACH NUMBER - 1 THE MOST BRUTE FORCE APPROACH 
// IN THIS APPROACH WE WILL SIMPLY USE THE BUILT-IN FUNCTION PRESENT IN THE C++ - pow(a,b)
// ALTHOUGH IT WILL GIVE THE O(1) TIME AND SPACE COMPLEXITY BUT THIS IS NOT THE MOST OPTIMAL APPROACH FROM INTERVIEW PERSPECTIVE

class Solution {
public:
    double myPow(double x, int n) {
        return pow(x,n);
    }
};





//APPROACH NUMBER - 2 THE RECURSION + MATHS APPROACH 

class Solution {
public:
    double myPow(double x, int n) {
        if(n==1) return x;   //base case for n=1
        if(n==0) return 1;  //base case for n=0 
        if(n<0) return 1/myPow(x,-(long long)n); //base case for n<0(negative)
        double half = myPow(x, n / 2);   //recursive case
        if(n%2==0)
        {
            return half*half;
        }

        return half*half*x;
    }
};