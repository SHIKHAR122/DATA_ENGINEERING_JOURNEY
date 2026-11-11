// GFG QUESTION NUMBER 4 - NEXT GREATER ELEMENTS


// You are given an array arr[] of integers, the task is to find the next greater for each element of the array in order of their appearance in the array. Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
// If there does not exist next greater of current element, then next greater element for current element is -1.

//pop  ->  mark the answer -> push 

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
                nums[n-1]=-1;       //marking the last element as -1 as there will be no greater element to its right
                st.push(arr[n-1]);      //pushing it to the stack as the top element
                for(int i=n-2;i>=0;i--)
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