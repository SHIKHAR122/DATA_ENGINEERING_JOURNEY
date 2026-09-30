// LEETCODE PROBLEM NUMBER 17 - LETTER COMBINATIONS OF A PHONE NUMBER




class Solution {
public:
    void func(string digits , string ans , vector<string>&final_output ,int index , map<char,string>&mp)
    {
        if(index>=digits.size())
        {
            
            final_output.push_back(ans);
            return;
        }
        string val=mp[digits[index]];   //will be storing the values from the hashmap  "123"
        for(int i=0;i<val.length();i++)
        {
            
            func(digits,ans+val[i],final_output,index+1,mp);
        }
    }
    vector<string> letterCombinations(string digits) {
        vector<string>final_output;  //final o/p which will be returned
        string ans="";  //to store the temporary results while backtracking
        int index=0;
        map<char,string>mp;
        mp['2'] = "abc";     
        mp['3'] = "def";
        mp['4'] = "ghi";
        mp['5'] = "jkl";
        mp['6'] = "mno";
        mp['7'] = "pqrs";
        mp['8'] = "tuv";         
        mp['9'] = "wxyz";
        func(digits,ans,final_output,index,mp);
        return final_output;
    }
};