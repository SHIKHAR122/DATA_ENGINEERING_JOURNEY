// GFG PROBLEM NUMBER 4 - COUNT THE SUBSEQUENCE WITH SUM 'K'


// FOR THIS PROBLEM WE WILL SOLVE THIS BY USING THE PREVIOUS APPROACH USING THE SAME LOGIC , THE ONLY DIFFERENCE WILL BE THAT IN THE LAT QUESTION WE WERE 
// RETURNING taken||notTaken , BUT IN THIS QUESTION WE WILL SIMPLY RETURN taken+notTaken.

#include<bits/stdc++.h>
using namespace std;


class Solution
{
    public:
            int subs(vector<int>&nums ,int k , int sum ,int index)
            {
                int n=nums.size();
                if(index == n)
                return sum == k;
                int l=subs(nums , k , sum+nums[index],index+1);
                int r=subs(nums , k  , sum , index+1);
                return l+r;
            }
};
int main()
{
    vector<int>nums={4, 9, 2, 5, 1};
    int index=0;
    int sum=0;
    int k=10;
    Solution sol;
    int res= sol.subs(nums,k,sum,index);
    cout<<res<<endl;
    
}