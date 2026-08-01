// LEETCODE PROBLEM NUMBER 1781 - SUM OF BEAUTY OF ALL SUBSTRING


//IN THIS PROBLEM WE WILL MANTAIN AN UNORDERED MAP , THAT WILL STORE THE FREQUENCY OF EACH CHARACTER WHILE MANTAINING A RUNNING SUM
//OF THE BEAUTY OF ALL THE SUBSTRING OF THE STRING 


class Solution {
public:
    int beautySum(string s) {
        int beauty=0;
        int n=s.size();
        for(int i=0;i<n;i++)
        {
          unordered_map<char , int >mp;
            for(int j=i;j<n;j++)
            {
                mp[s[j]]++;
                int minimum=INT_MAX;
                int maximum=INT_MIN;
                for(auto it: mp)
                {
                    minimum=min(minimum , it.second);
                    maximum=max(maximum,it.second);

                }
                beauty+=(maximum-minimum);
            }
        }
        return beauty;
    }
};