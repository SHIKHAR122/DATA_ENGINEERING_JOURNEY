// LEETCODE PROBLEM NUMBER 155 - MIN STACK 
#include<bits/stdc++.h>
using namespace std;

class MinStack
{
public:
    stack<long long> st;
    long long minimum;

    MinStack()
    {
        minimum = LLONG_MAX;
    }

    void push(int value)
    {
        long long x = (long long)value;

        if(st.empty())
        {
            st.push(x);
            minimum = x;
        }
        else if(x >= minimum)
        {
            st.push(x);
        }
        else
        {
            st.push(2*x - minimum);
            minimum = x;
        }
    }

    void pop()
    {
        if(st.empty()) return;

        if(st.top() < minimum)
        {
            long long old_minimum = 2*minimum - st.top();
            minimum = old_minimum;
        }

        st.pop();

        if(st.empty())
            minimum = LLONG_MAX;
    }

    int top()
    {
        if(st.empty()) return -1;

        if(st.top() < minimum)
            return (int)minimum;
        else
            return (int)st.top();
    }

    int getMin()
    {
        if(st.empty()) return -1;

        return (int)minimum;
    }
};

int main()
{
    MinStack st;

    st.push(-2);
    st.push(0);
    st.push(-3);

    cout << "Current Minimum: " << st.getMin() << endl;

    st.pop();

    cout << "Top Element: " << st.top() << endl;
    cout << "Current Minimum: " << st.getMin() << endl;

    st.pop();

    cout << "Top Element: " << st.top() << endl;
    cout << "Current Minimum: " << st.getMin() << endl;

    return 0;
}
