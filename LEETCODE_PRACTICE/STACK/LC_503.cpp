// LEETCODE PROBLEM NUMBER 503 - NEXT GREATER ELEMENT 2 

#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public: 
            vector<int> nextGreaterElements(vector<int>& nums) {
                int n=nums.size();
                stack<int>st;
                vector<int>ans(n,-1);
                for(int i=2*n-1;i>=0;i--)
                {
                    int index = i%n;
                    while(!st.empty() && st.top()<=nums[index])
                    {
                        st.pop();
                    }
                    if(i<n && !st.empty())
                    {
                        ans[index]=st.top();
                    }
                    st.push(nums[index]);
                }
                return ans;
    }
};

int main()
{
    vector<int>nums={1,2,3,4,3};
    Solution sol;
    vector<int>res=sol.nextGreaterElements(nums);
    for(int i=0;i<res.size();i++)
    {
        cout<<res[i]<<endl;

    }
}