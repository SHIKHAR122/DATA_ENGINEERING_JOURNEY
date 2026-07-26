// LEETCODE PROBLEM NUMBER 796 - ROTATE STRING 


//APPROACH NUMBER 1 - ITERATING THROUGH EACH STRING GIVEN AND CHECK FOR THE GIVEN GOAL
//THIS IS THE BRUTE FORCE APPROACH OF THE GIVEN PROBLEM

class Solution {
public:
    bool rotateString(string s, string goal) {
        if(s.size() != goal.size()) return false;
        for(int i=0;i<s.length();i++)
        {
            s = s.substr(1) + s[0];
            if(s==goal)
            {
                return true;
            }
        }
        return false;
    }
};




//APPROACH NUMBER 2 - CONCATINATING THE STRING TWICE AND THEN LOOKING FOR THE RESULT IN THE CONCATINATED STRING -
//THIS IS THE OPTIMAL SOLUTION OF THE PROBLEM 

class Solution {
public:
    bool rotateString(string s, string goal) {
        if(s.size()!=goal.size()) return false;
        string doubled=s+s;
        return doubled.find(goal)!=string::npos;
    }
};