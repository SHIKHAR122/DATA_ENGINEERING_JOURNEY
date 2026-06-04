// LEETCODE PROBLEM NUMBER - 560 SUBARRAY SUMS EQUAL 'K'
// IN THIS PROBLME WE WILL BE USING A HASH MAP AND THEN FOR THE 'SUM-K' VALUE , WE'LL TRY TO SEARCH FOR IT , 
//IF YES THEN COUNT IF NO THEN REGISTER IN THE HASHMAP


class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        mp[0] = 1;  
        int sum = 0, count = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            if (mp.count(sum - k))
                count += mp[sum - k];
                mp[sum]++;
        }
        return count;
    }
};