//  LEETCODE PROBLEM NUMBER 151 - REVERSE WORDS IN A STRING

//APPROACH NUMBER  1  

//IN THIS APPROACH WE WILL USE STRINGSTREAM FUNCTION TO GET THE WORDS , THEN STORE IT IN THE VECTOR WHICH WILL BE FURTHER REVERSED
// AND THEN EACH STRING WILL BE CHECKED FOR HANDLING THE SPACES 

// TIME COMPLEXITY - O(n)
#include<string>
class Solution {
public:
    string reverseWords(string s) {
        string ans="";
        string word;
        vector<string>words;
        stringstream ss (s);
        while(ss>>word)
        {
            words.push_back(word);
        }
        reverse(words.begin() , words.end());

        for(string w : words)
        {
            if(ans.empty())
            {
                ans.append(w);
            }
            else{
                ans.append(" ");
                ans.append(w);
            }
        }
        return ans;
    }
};





// APPROACH NUMBER 2 -- USING THE STACK DATA STRUCTURE

// IN THIS APPROACH WE WILL SIMPLY USE STRING STREAMTO FETCH EACH WORD AND THEN SIMPLY PUSH IT INTO STACK AND THEN PUSH IT BACK 
// INTO THE STRING 



class Solution {
public:
    string reverseWords(string s) {
        stack<string>st;
        string ans ="";
        string word;
        stringstream ss (s);
        while(ss>>word)
        {
            st.push(word);
        }
        while(!st.empty())
        {   
            if(ans.empty())
            {
                ans.append(st.top());
                st.pop();
            }
            else {
                ans.append(" ");
                ans.append(st.top());
                st.pop();
            }
        }   
        return ans;
    }
};