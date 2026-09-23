// GFG PROBLEM - REVERSE A STACK
// APPROACH NUMBER 1 - IN THIS APPROACH WE ARE USING THE EXTRA SPACE COMPLEXITY BY USING A VECTOR TO REVERSE THE STACK.
#include<bits/stdc++.h>
using namespace std;
class Solution {
  public:
    void reverseStack(stack<int> &st) {
        
        vector<int>ans;
        while(!st.empty())
        {
            int elem=st.top();
            ans.push_back(elem);
            st.pop();
        }
        for(int i=0;i<ans.size();i++)
        {
            st.push(ans[i]);
        }
    }
};

int main()
{
    stack<int> st;
    Solution sol;
    sol.reverseStack(st);

}


// APPROACH NUMBER 2 - USING THE RECURSIVE APPROACH -
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:

    void insertAtBottom(stack<int>& st, int x)
    {
        // Base case
        if(st.empty())
        {
            st.push(x);
            return;
        }

        int top = st.top();
        st.pop();

        insertAtBottom(st, x);

        st.push(top);
    }

    void reverseStack(stack<int>& st)
    {
        // Base case
        if(st.empty())
            return;

        int top = st.top();
        st.pop();

        reverseStack(st);

        insertAtBottom(st, top);
    }
};

int main()
{
    stack<int> st;

    st.push(1);
    st.push(2);
    st.push(3);
    st.push(4);

    Solution obj;
    obj.reverseStack(st);

    while(!st.empty())
    {
        cout << st.top() << " ";
        st.pop();
    }

    return 0;
}