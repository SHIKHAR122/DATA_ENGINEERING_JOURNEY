#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
           int maxSum(vector<int>&nums,  int k)
           {
                int prevsum=0;
                int sum=0;
                int maxsum=INT_MIN;
                for(int i=0;i<k;i++)
                {       
                    prevsum+=nums[i];
                }
                int currentsum=0;
                int i=1;
                int j=k;
                int n=nums.size();
                // maxsum=prevsum;
                while(j<n)
                {
                    currentsum=prevsum+nums[j]-nums[i-1];
                    if(currentsum>maxsum)
                    {       
                        maxsum=currentsum;
                    }
                    prevsum=currentsum;
                    i++;
                    j++;
                }
                return maxsum;
           }
};
int main()
{
    Solution sol;
    vector<int>nums={7,1,2,5,8,4,9,3,6};
    int k;
    int n;
    cout<<"ENTER THE SIZE OF THE ARRAY: ";
    cin>>n;
    cout<<"ENTER THE SIZE OF 'k' : ";
    cin>>k;
    cout<<"THE MAXIMUM SUM OF THE SUBARRAY OF SIZE K IS : "<<sol.maxSum(nums , k);
}
