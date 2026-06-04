// LEETCODE PROBLEM NUMBER - 136 SINGLE NUMBER 
// IN THIS QUESTION WE SIMPLY EITHER USE THE HASH MAP OR WE CAN ALSO GO WITH THE XOR LOGIC (I HAVE USED HASHMAP LOGIC FOR NOW)
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int,int>mp;
        for(auto x : nums)
        {
            mp[x]++;
        }
        for(auto it: mp)
        {
            if(it.second==1)
            {
                return it.first;
            }
        }
        return 1;
    }
};