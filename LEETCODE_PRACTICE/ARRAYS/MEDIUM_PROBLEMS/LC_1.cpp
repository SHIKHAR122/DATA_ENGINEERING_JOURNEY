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



//APPROACH NUMBER 2 - USING THE HASHMAP APPROACH - 

//THIS APPROACH WILL HAVE COMPLEXITY OF O(n)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n =nums.size();
        unordered_map<int, int> numMap;
        int complement;
        for(int i =0 ;i<nums.size();i++){
            complement=target-nums[i];
            if(numMap.count(complement))
            {
                return {numMap[complement],i};
            }
                numMap[nums[i]]=i;
        }  
        return {}; 
    }
};