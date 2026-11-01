// LEETCODE PROBLEM NUMBER 1248 - COUNT NUMBER OF NICE SUBARRAYS


#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public:
        int atmost(vector<int>&nums , int k)
    {
        int count=0;
        int oddcount=0;
        int left=0;
        int n=nums.size();
        for(int right=0;right<n;right++)
        {
            if(nums[right]%2!=0)   //if the current element is an odd element
            {
                oddcount++;  //increase the count of the odd elements
            }
            while(oddcount>k)   //condition for shrinking the window
            {   
                if(nums[left]%2!=0)  //if the element is an odd number so decrease the count
                {
                    oddcount--;
                }
                left++;
            }
            count=count+(right-left+1);  //calculating the final count of the digits
        }
        return count ;
    }
    int numberOfSubarrays(vector<int>& nums, int k) {
        return atmost(nums , k)-atmost(nums , k-1);
    }
};
int main()
{
    Solution sol;
    vector<int>nums;
    int k;
    sol.numberOfSubarrays(nums , k);
}