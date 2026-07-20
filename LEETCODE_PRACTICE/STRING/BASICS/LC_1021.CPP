// LEETCODE PROBLEM NUMBER 1021 -  REMOVE OUTER PARANTHESES


//  IN THIS QUESTION WE WILL USE A STACK TO VALIDATE THE OUTER PARANTHESES 

//COMPLEXITY - O(N) RUNTIME AND O(N) SPACE  

class Solution {
public:
    string removeOuterParentheses(string s) {
        stack<char> st;
        string ans = "";

        for (char ch : s) {
            if (ch == '(') {
                if (!st.empty()) {
                    ans.push_back(ch);
                }
                st.push(ch);
            } else { // ch == ')'
                st.pop();
                if (!st.empty()) {
                    ans.push_back(ch);
                }
            }
        }

        return ans;
    }
};




// APPROACH NUMBER 2 -  USING THE COUNTERS

// IN THIS APPROACH WE WILL USE COUNTER ----> +1 FOR '('   AND    -1 FOR ')'


//COMPLEXITY IS O(1)

class Solution {
public:
    string removeOuterParentheses(string s) {
        string ans="";
        int count=0;
        for(char ch: s)
        {
            if(ch=='(')
            {
                if(count>0)
                {
                    ans.push_back(ch);
                }
                 count++;
            }
            else {
                count--;
                if(count>0)
                {
                    ans.push_back(ch);
                }
            }
        }
        return ans ; 
    }
};