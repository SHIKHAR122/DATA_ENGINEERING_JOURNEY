//LEETCODE PROBLEM NUMBER - 169 MAJORITY ELEMENTS -I 
// IN THIS PROBLEM WE USE THE MOORE'S VOTING ALGORITHM TO FIND THE GREATEST COUNT 

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int c=INT_MIN;
        int count=0;
        for(auto num: nums)
        {
            if(count==0) c=num;
            if(num==c) count++;
            else count--;
        }
        return c;
    }
};





//ANOTHER APPROACH TO SOLVE THE PROBLEM IS BY USING THE UNORDERED MAP

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int>mp;
        int greatest_freq;
        int greatest_num;
        for(auto it :  nums)
        {   
            mp[it]++;
        }
        for(auto &x: mp)
        {
            if(x.second>greatest_freq)
            {
                greatest_freq=x.second;
                greatest_num=x.first;
            }

        }
        return greatest_num;
    }
};