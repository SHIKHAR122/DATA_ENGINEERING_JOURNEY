// LEETCODE PROBLEM NUMBER 1944 - NUMBER OF VISIBLE PEOPLE IN THE QUEUE 

// APPROACH NUMBER 1 - THE BRUTE FORCE APPROACH 
//TIME COMPLEXITY WILL BE O(N^2) AND THE SPACE COMPLEXITY WILL BE O(n)

#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public: 
          vector<int> canSeePersonsCount(vector<int>& heights) {

        int n = heights.size();
        vector<int> ans;

        for(int i = 0; i < n; i++)
        {
            int count = 0;
            int maxHeight = 0;

            for(int j = i + 1; j < n; j++)
            {
                if(heights[j] > maxHeight)
                {
                    count++;
                    maxHeight = heights[j];
                }

                if(heights[j] >= heights[i])
                    break;
            }

            ans.push_back(count);
        }

        return ans;
    }
};
int main  ()
{
    vector<int>heights={10,5,8,6,11,9};
    Solution sol;
   vector<int>ans= sol.canSeePersonsCount(heights);
   for(int i=0;i<ans.size();i++)
   {    
        cout<<ans[i]<<" ";
   }
}




// APPROACH NUMBER 2 - USING MONOTONIC  DECREASING STACK 

//TIME COMPLEXITY - O(n)

#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public: 
          vector<int> canSeePersonsCount(vector<int>& heights) {
            stack<int>st;
            int n=heights.size();
            vector<int>ans(n,0);
            for(int i=0;i<n;i++){
                while(!st.empty()  && heights[i]>heights[st.top()])  //if the current element's height is greater than the height of the element at the stack's top index 
                {
                    ans[st.top()]++;   //increase its count in the resultant vector
                    st.pop();          //pop  it 
                }
                if(!st.empty())
                {
                    ans[st.top()]++;
                }
                st.push(i);       
            }   
            return ans;
    }
};
int main  ()
{
    vector<int>heights={10,5,8,6,11,9};
    Solution sol;
   vector<int>ans= sol.canSeePersonsCount(heights);
   for(int i=0;i<ans.size();i++)
   {    
        cout<<ans[i]<<" ";
   }
}