// CHECK IF THE ARRAY CAN BE PARTITIONED INTO TWO CONTINUOS ARRAYS OF EQUAL SUM
#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
          bool partition(vector<int>&nums)
          {
             int n=nums.size();
             int x;
             for(int i=1;i<n;i++)  //formation of the prefix sum of the given array
             {
                nums[i]+=nums[i-1];
             }
             for(int i=1;i<n;i++)  //checking that if there exist an element who matches the condition then return it 
             {
                if(2*nums[i]==nums[i-1])
                {
                    return true;
                }
             }
             return false;
          }
};
int main()
{
    vector<int>nums={1,2,3,4,5,6,7,8,9,10,11,12,1,13};
    Solution sol;
    cout<<sol.partition(nums);
}
