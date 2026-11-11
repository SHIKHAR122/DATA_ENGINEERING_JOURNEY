// GFG QUESTION NUMBER 5 - PREVIOUS GREATER ELEMENTS


// You are given an integer array arr[]. For every element in the array, determine its Previous Greater Element (PGE).

// The Previous Greater Element (PGE) of an element x is the first element that appears to the left of x in the array and is strictly greater than x.


// Note: If no such element exists, assign -1 as the PGE for that position.



#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public:
           vector<int>NextGreater(vector<int>&arr)
           {
                stack<int>st;
                int n=arr.size();
                vector<int>nums(n);   //resultant vector of the same size as that  of the original one 
                nums[0]=-1;       //marking the last element as -1 as there will be no greater element to its right
                st.push(arr[0]);      //pushing it to the stack as the top element
                for(int i=1;i<=n-1;i++)
                {
                    while(st.size()>0 && st.top()<=arr[i])   //if the element at the top is lesser than the array's element then we will pop it 
                    {
                        st.pop();
                    }
                    if(st.size()==0)   //if the stack gets empty then simply push -1 to the resultant vector
                    {   
                        nums[i]=-1;
                    }
                    else{
                        nums[i]=st.top();  //if it is not empty then the stack's top element should be writtten in the resultant vector
                    }
                    st.push(arr[i]);  //last step is to push that current element of the array to the stack
                }
                return nums;
           }
};
int main()
{
    vector<int>arr={3,1,2,5,4,6,2,3};
    Solution sol;
    vector<int> ans = sol.NextGreater(arr);
    for(int i = 0; i < ans.size(); i++)
    {
        cout << ans[i] << " ";
    }
}