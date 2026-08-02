// LEETCODE PROBLEM NUMBER 3 LONGEST SUBSTRING WITHOUT REPEATING THE CHARACTERS 


//APPROACH NUMBER 1 - BRUTE FORCE APPROACH 
// IN THIS APPROACH WE WILL USE NESTED LOOPING AND A HASHMAP TO CHECK FOR THE EXISTENCE OF ANY GIVEN CHARACTER AND
// ALSO MAINTAINING THE LONGEST SUBSTRING , AS SOON AS WE ENCOUNTER A CHARACTER WHICH ALREADY EXISTED IN THE MAP WE WILL BREAK
// THROUGH THE LOOP AND RETURN THE PREVIOUS LONGEST SUBSTRING


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        int ans = 0;
        if(n==0) return 0;
        if(s==" ") return 1;
        for (int i = 0; i < n; i++) {
            unordered_map<char, int> mp;
            for (int j = i; j < n; j++) {
                if (mp.count(s[j])) {
                    break;
                }
                mp[s[j]] = 1;
                ans = max(ans, j - i + 1);
            }
        }

        return ans;
    }
};

// NOTE THAT THIS APPROACH IS NOT AN OPTIMAL APPROACH AS FOR THE s.length <= 5*10^4 CONSTRAINT , THIS APPROACH WILL GIVE TLE 



// THUS WE HAVE TO OPTIMIZE THIS APPROACH BY HANDLING THE INNER LOOP SOMEHOW 

