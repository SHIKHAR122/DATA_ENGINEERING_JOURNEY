//LEETCODE PROBLEM NUMBER 128- FIND THE LONGEST CONSECUTIVE SEQUENCE
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        int count=0;
        int longest=0;
        int x ;
        unordered_set<int>st(nums.begin(),nums.end());
        if(n==0) return 0;
        for(int i=0;i<n;i++)
        {
            st.insert(nums[i]);
        }
        for(auto num : st)
        {
            if(st.find(num-1)==st.end())
            {
                x=num;
                count=1;
                while(st.find(x+1)!=st.end())
                {
                    x++;
                    count++;
                }
                longest=max(longest,count);
            }
        }
        return longest;
    }
};