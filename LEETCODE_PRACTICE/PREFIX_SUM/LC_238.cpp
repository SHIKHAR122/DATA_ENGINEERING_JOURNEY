// LEETCODE PROBLEM NUMBER 238 - PRODUCT OF NUMBERS EXCEPT ITSELF
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> PrefixSuffix(vector<int>& nums, int n) {
        vector<int> ans(n);
        vector<int> prefix(n);
        vector<int> suffix(n);

        int p = 1;
        prefix[0] = 1;

        for (int i = 1; i < n; i++) {
            p *= nums[i - 1];
            prefix[i] = p;
        }

        int s = 1;
        suffix[n - 1] = 1;

        for (int i = n - 2; i >= 0; i--) {
            s *= nums[i  + 1];
            suffix[i] = s;
        }

        for (int i = 0; i < n; i++) {
            ans[i] = suffix[i] * prefix[i];
        }

        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 4};
    int n = nums.size();

    vector<int> ans = sol.PrefixSuffix(nums, n);

    for (int x : ans) {
        cout << x << " ";
    }

    return 0;
}
