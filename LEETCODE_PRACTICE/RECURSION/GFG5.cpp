// GFG PROBLEM NUMBER 5 - GENERATE BINARY STRINGS WITHOUT CONSECUTIVE 1s


// THIS PROBLEM IS SOLVED RECURSIVELY WHERE WE ARE APPEDING 0 IN THE FIRST CALL AND 1 IN THE ANOTHER CALL KEEPING IN MIND THAT IF THERE IS 
// ALREADY A 1 IN THE BACK OF THE STRING THEN DONT APPEND THE 1 OTHERWISE APPEND IT -



class Solution {
public:
    void func(vector<string>&result , string ans , int n)
    {
        if(ans.size()==n)
        {
            result.push_back(ans);
            return;
        }
        ans.push_back('0');
        func(result,ans,n);
        ans.pop_back();
        if(ans.back()!='1'||ans.empty())
        {
            ans.push_back('1');
            func(result,ans ,n);
            ans.pop_back();
        }

    }
    vector<string> generateBinaryStrings(int n) {
        // Your code goes here
        vector<string>result;
        string ans="";
        func(result,ans,n);
        return result;
    }
};
