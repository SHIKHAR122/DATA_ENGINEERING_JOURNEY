// LEET CODE PROBLEM NUMBER 69  - SQRT(X)
// IN THIS PROBLEM WE HAVE TO RETURN THE SQAURE ROOR VALUE OF THE GIVEN INTEGER - X 

class Solution {
public:
    int mySqrt(int x) {
        int low=0;
        int high=x;
        while(low<=high)
        {
            int mid=low+(high-low)/2;
            long long sq= 1LL * mid * mid ;
            if(sq==x)
            {
                return mid;
            }
            else if(sq<x)
            {
                low=mid+1;
            }
            else {
                high=mid-1;
            }
        }
        return high;
    }
};