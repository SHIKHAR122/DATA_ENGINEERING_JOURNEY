// LEETCODE PROBLEM NUMBER 1903 - LARGEST ODD NUMBER IN A STRING 



// IN THIS PROBLEM WE WILL TRAVERSE FROM THE LAST AND AS SOON AS WE ENCOUNTER THE FIRST ODD NUMBER WE WILL APPEND THE STRING FROM THE 
//STARTING TILL THAT INDEX ONLY , THAT WILL BE OUR ANSWER

class Solution {
public:
    string largestOddNumber(string num) {
        string ans="";
        for(int i=num.length()-1;i>=0;i--)
        {   
            int digit= num[i]-'0';
            if(digit%2==1)
            {
                ans.append(num.substr(0,i+1));
                break; 
            }
        }
        return ans ;
    }
};