// GFG QUESTION NUMBER 6 - STOCK SPAN PROBLEM 


#include<bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<int> StockSpan(vector<int>& arr)
    {
        stack<int> st;
        int n = arr.size();
        vector<int> res(n);
        for(int i = 0; i < n; i++)
        {
            while(!st.empty() && arr[st.top()] <= arr[i])
            {
                st.pop();
            }
            if(st.empty())
            {
                res[i] = i + 1;
            }
            else
            {
                res[i] = i - st.top();
            }
            st.push(i);
        }
        return res;
    }
};

int main()
{
    vector<int> arr{100, 80, 90, 120};
    Solution sol;
    vector<int> ans = sol.StockSpan(arr);
    for(int x : ans)
    {
        cout << x << " ";
    }
}