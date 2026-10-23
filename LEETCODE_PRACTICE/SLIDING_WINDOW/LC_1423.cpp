#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
        int maxScore(vector<int>& cardPoints, int k) {
        int n = cardPoints.size();
        int current_sum = 0;
        
        // Step 1: Sum the first k cards from the left
        for (int i = 0; i < k; i++) {
            current_sum += cardPoints[i];
        }
        
        int max_sum = current_sum;
        
        // Step 2: Gradually remove cards from the left and add from the right
        for (int i = 0; i < k; i++) {
            current_sum -= cardPoints[k - 1 - i]; // Remove from left window
            current_sum += cardPoints[n - 1 - i]; // Add from the right end
            max_sum = max(max_sum, current_sum);
        }
        
        return max_sum;
    }
};
int main()
{
    Solution sol;
    vector<int>cardPoints={1,2,3,4,5,6,1};
    int k=3;
    sol.maxScore(cardPoints ,k);
}