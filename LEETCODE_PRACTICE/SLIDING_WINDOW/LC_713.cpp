// LEETCODE PROBLEM NUMBER 713 - SUBARRAY PRODUCT LESS THAN 'K'


#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public:
          int minimumSubarray(vector<int>&nums , int k)
          {
             int i=0;
             int j=0;
             int n=nums.size();
             int count=0;
             int prod=1;
             if(k<=1) return 0;
             while(j<n)
             {
                prod*=nums[j];
                while(prod>=k)
                {
                    prod/=nums[i];
                    i++;
                }
                count+=(j-i+1);
                j++;
             }
             return count;
          }
};
int main ()
{
    Solution sol;
    vector<int>nums;
    cout<<"ENTER THE ARRAY ELEMENTS : ";
    for(int i=0;i<nums.size();i++)
    {
        cin>>nums[i];
    }
    int k;
    cout<<"ENTER THE kth ELEMENT : ";
    cin>>k;
    cout<<sol.minimumSubarray(nums , k);
}