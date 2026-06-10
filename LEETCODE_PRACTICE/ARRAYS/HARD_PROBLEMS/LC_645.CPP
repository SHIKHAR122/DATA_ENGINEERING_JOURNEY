// LEETCODE PROBLEM NUMBER 645 - SET MISMATCH

// THIS QUESTION CAN BE SOLVED USING THREE APPROACHES


// APPROACH NUMBER 1 IS USING THE UNORDERED MAP AND STORING  THE FREQUENCIES , IF THE FREQ. IS 
// 0 OR 2 .... THEN IT IS TO BE RETURNED
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        unordered_map<int,int>mp;
        for(int i =0;i<nums.size();i++)
        {
            mp[nums[i]]++;
        }
        int missing =-1;
        int repeat=-1;
        for(int i =1 ;i<=nums.size();i++)
        {
            if(mp[i]==2)
            {
                repeat=i;
            }
            if(mp[i]==0){
                missing=i;
            }   
        }
        return{repeat,missing};
    }
};



// APPROACH 2 IS UISNG THE HASH SET OR HASH SET 
