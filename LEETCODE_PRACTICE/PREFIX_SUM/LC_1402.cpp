// LEETCODE PROBLEM NUMBER 1402 - REDUCING DISHES 

// 1. Sort the satisfaction array in descending order (best dishes first).
// 2. Iterate through the array while maintaining a running current_sum of the selected dishes.
// 3. The Greedy Rule: Add current_sum to your total max_sum at each step.
// 4. Stop condition: The moment current_sum becomes negative, stop adding dishes because any remaining smaller dishes will only pull your total score down.


#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        int n=satisfaction.size();
        vector<int>suffixSum(n);
        sort(satisfaction.begin() , satisfaction.end());
        suffixSum[n-1]=satisfaction[n-1];
        for(int i=n-2;i>=0;i--)
        {
            suffixSum[i]=suffixSum[i+1]+satisfaction[i];
            //current element = aage wala element+given vector ka current element 
        }
        // find the index where we encounter the first positivi value 
        int index=-1;
        for(int i=0;i<n;i++)
        {
            if(suffixSum[i]>=0)
            {
                index=i;
                break;
            }
        }
        if(index==-1) return 0;
        //calculate the maximum sum
        int max_sum=0;
        int x=1;
        for(int i=index;i<n;i++)
        {
            max_sum+=(satisfaction[i]*x);
            x++;
        }
        return max_sum;
    }
};

int main()
{
    Solution sol;
    vector<int>satisfaction;
    cout<<sol.maxSatisfaction(satisfaction);
}