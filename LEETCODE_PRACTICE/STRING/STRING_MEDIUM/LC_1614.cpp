// LEETCODE PROBLEM NUMBER 1614 - MAXIMUM NESTING DEPTH OF THE PARANTHESES


// APPROACH NUMBER 1 IN THIS APPROACH WE WILL SIMPLY INITIALIZE 2 VARIABLES - COUNT AND MAXDEPTH , 
// THEN FOR EVERY OCCURENCE OF - '(' WE WILL INCREMENT THE COUNT AND FOR EVERY ')' WE WILL DECREMENT IT , 
//  THEN SIMPLY USE THE MAXDEPTH TO FIND THE MAXIMUM DEPTH OF THE PARANTHESES



class Solution {
public:
    int maxDepth(string s) {
        int count=0;
        int maxDepth=0;
        for(char ch : s)
        {
            if(ch=='(')
            {
                count++;
            }
            else if(ch==')')
            {
                count--;
            }
            maxDepth=max(maxDepth , count);
        }
        return maxDepth;
    }

};




// APPROACH NUMBER 2 - USING STACK 
// IN THIS APPROACH WE WILL USE THE STACK TO MANTAIN THE RECORD OF THE DEEPEST NESTED PARENTHSES , WHERE 
// IF THE '(' IS ENCOUNTERED , WE WILL SIMPLY PUSH IT , CALCULATE THE MAX DEPTH AND IF THE PARANTHSES IS- ')' , THEN POP THE STACKTOP




class Solution {
public:
    int maxDepth(string s) {
        stack<char>st;
        int maxDepth=0;
        for(char ch : s)
        {
            if(ch=='(')
            {
                st.push(ch);
                maxDepth=max(maxDepth , (int)st.size());
            }  
            else if(ch==')')
            {
                st.pop();
            } 
        }
        return maxDepth;
    }
};