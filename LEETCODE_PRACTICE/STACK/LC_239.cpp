// LEETCODE PROBLEM NUMBER 239 - SLIDING WINDOW MAXIMUM 


// APPROACH NUMBER 1 - THE BRUTE FORCE APPROACH 
// TIME COMPLEXITY -  O(n^2)
#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public:
           vector<int>SlidingWindow(vector<int>&nums , int k)
           {
                int n=nums.size();
                vector<int>ans;
                for(int i=0;i<n-k;i++)
                {
                    int maximum=nums[0];
                    for(int j=i;j<i+k-1)
                    {
                        if(nums[j]>maximum)
                        {
                            maximum=max(maximum , nums[j]);
                        }
                        ans.push_back(maximum);
                    }
                }
                return ans ;
           }
};
int main ()
{
    vector<int>nums={1,3,-1,-3,5,3,6,7};
    int k=3;
    Solution sol;
    vector<int>ans=sol.SlidingWindow(nums , k);
    for(int i=0;i<ans.size();i++)
    {
        cout<<ans[i]<<" ";
    }
}   





// APPROACH NUMBER 2 - THE OPTIMAL SOLUTION 

