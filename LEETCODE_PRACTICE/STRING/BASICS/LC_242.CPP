// LEETCODE PROBLEM NUMBER 242 - VALID ANAGRAM 

// APPROACH NUMBER 1 - THE BRUTE FORCE APPROACH 
// IN THIS APPROACH WE WILL SORT BOTH THE STRING ANS THEN COMAPARE THEM IF THEY WILL BE SAME WE WILL GET TRUE ELSE FALSE 
//COMPLEXITY OF THE CODE IS - O (log N )
class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin() , s.end());
        sort(t.begin(), t.end());
        return s==t;
    }
};



//APPROACH NUMBER 2  - UISNG THE UNORORDERED MAP 
//IN THIS APPROACH WE WILL STORE THE ELEMENTS OF BOTH THE ELEMENTS IN 2 DIFEFERENT MAPS AND THEN COMPARE THOSE MAPS 
// COMPLEXITY -  O(n)
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<int,int>S;
        unordered_map<int ,int>T;
        if(s.size()!=t.size()) return false;
        for(int i =0 ; i<s.size();i++)
        {
            T[t[i]]++;
            S[s[i]]++;
        }
        return T==S;
    }
};
