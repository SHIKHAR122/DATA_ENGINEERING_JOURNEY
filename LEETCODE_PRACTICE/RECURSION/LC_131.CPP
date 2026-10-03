// LEETCODE PROBLEM NUMBER 131 - PALINDROME PARTITIONING


class Solution {
public:
    bool isPalin(string &s , int left , int right)   //function for checking if the substring is a palindrome or not 
    {
        while(left<right)
        {
            if(s[left]!=s[right])
            {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
    void func(string s , int index , vector<string>&current , vector<vector<string>>&result)
    {
        if(index==s.size())
        {
            result.push_back(current);
            return;
        }
        for(int i=index;i<s.size();i++)
        {
            if(isPalin(s,index,i))
            {
                current.push_back(s.substr(index,i-index+1));
                func(s,i+1,current,result);
                current.pop_back();
            }
        }
    }

    vector<vector<string>> partition(string s) {
        vector<vector<string>>result;
        int index=0;
        vector<string>current;
        func(s,index,current,result);
        return result;
    }
};