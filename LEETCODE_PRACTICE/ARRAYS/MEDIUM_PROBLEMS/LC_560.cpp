//LEETCODE PROBLEM NUMBER 560  SUBARRAY SUMS EQUALS K (COUNT OF THE SUBARRAY SUM)
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int>mp;
        mp[0]=1;
        int psum=0;
        int count=0;
        for(int i =0;i<nums.size();i++)
        {
            psum+=nums[i]; //increase the prefix sum
            int remove=psum-k; //find the value to be excluded
            count+=mp[remove];//update the count
            mp[psum]+=1; //store in the hashmap
        }
        return count;
    }
};