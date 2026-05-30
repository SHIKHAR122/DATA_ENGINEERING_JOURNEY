// LEETCODE PROBLEM NUMBER - 01 TWO SUM 
// MAKE PAIRS OF THE VALUES(THE ARRAY INDEX AND THE INDEX VALUE ) AND THEN ADD THEM AND CHECK UISNG TWO POINTER APPROACH
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int sum=0;
        vector<pair<int,int>>pairsum;
        for(int i=0;i<nums.size();i++)
        {
            pairsum.push_back(make_pair(nums[i],i));
        }
        sort(pairsum.begin(),pairsum.end());
        int left=0;
        int right=pairsum.size()-1;
        while(left<right)
        {
            if((sum=pairsum[left].first+pairsum[right].first)==target)
            {
                return {pairsum[left].second,pairsuma[right].second};
            }
            else if(sum>target)
            {
                right--;
            }
            else
            {
                left++;
            }
        }
        return {};
    }
};