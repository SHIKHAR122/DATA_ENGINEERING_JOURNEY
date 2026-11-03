// LEETCODE PROBLEM NUMBER 1381 - DESING A  STACK WITH INCREMENT FUNCTION 
//  IN THIS PROBLEM WE HAVE TO IMPLEMENT A STACK USING THE ARRAY OR THE VECTOR DATA STRUCTURE
#include <bits/stdc++.h>
using namespace std;

class CustomStack {
public:
    vector<int> st;
    int n = 0;

    CustomStack(int maxSize) {
        n = maxSize;
    }

    void push(int x) {
        if (st.size() < n) {
            st.push_back(x);
        }
    }

    int pop() {
        if (st.empty()) {
            return -1;
        }
        else {
            int temp = st.back();
            st.pop_back();
            return temp;
        }
    }

    void increment(int k, int val) {
        int lim = min((int)st.size(), k);

        for (int i = 0; i < lim; i++) {
            st[i] += val;
        }
    }
};

int main() {

    CustomStack cs(3);

    cs.push(1);
    cs.push(2);

    cout << cs.pop() << endl;  // 2

    cs.push(2);
    cs.push(3);
    cs.push(4);  // Ignored because capacity is 3

    cs.increment(5, 100);

    cout << cs.pop() << endl;  // 103
    cout << cs.pop() << endl;  // 102
    cout << cs.pop() << endl;  // 101
    cout << cs.pop() << endl;  // -1

    return 0;
}
