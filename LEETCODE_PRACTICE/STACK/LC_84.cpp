// LEETCODE PROBLEM NUMBER 84 - LARGEST RECTANGLE IN THE HISTOGRAM 



#include<bits/stdc++.h>
using namespace std;
class Solution 
{   
    public:
        int largestRectangleArea(vector<int>& heights) {
            int n = heights.size();
            if(n == 0) return 0;
            stack<int> st;
            vector<int> nsi(n);
            nsi[n-1] = n;
            st.push(n-1);
            // Next Smaller Index
            for(int i = n-2; i >= 0; i--)
            {
                while(!st.empty() && heights[st.top()] >= heights[i])
                {
                    st.pop();
                }
                if(st.empty())
                {
                    nsi[i] = n;
                }
                else
                {
                    nsi[i] = st.top();
                }
                st.push(i);
            }
            stack<int> gt;
            vector<int> psi(n);
            psi[0] = -1;
            gt.push(0);
            // Previous Smaller Index
            for(int i = 1; i < n; i++)
            {
                while(!gt.empty() && heights[gt.top()] >= heights[i])
                {
                    gt.pop();
                }
                if(gt.empty())
                {
                    psi[i] = -1;
                }
                else
                {
                    psi[i] = gt.top();
                }
                gt.push(i);
            }
            // Calculate maximum area
            int maxarea = 0;
            for(int i = 0; i < n; i++)
            {
                int area = heights[i] * (nsi[i] - psi[i] - 1);
                maxarea = max(maxarea, area);
            }
            return maxarea;
    }
};  
int main ()
{
    int n;
    cout<<"ENTER THE SIZE OF THE ARRAY: ";
    cin>>n;
    vector<int>heights;
    cout<<"ENTER THE ARRAY ELEMENTS: ";
    for(int i=0;i<n;i++)
    {
        cin>>heights[i];
    }
    Solution sol;
    sol.LargestRectangle(heights);
}