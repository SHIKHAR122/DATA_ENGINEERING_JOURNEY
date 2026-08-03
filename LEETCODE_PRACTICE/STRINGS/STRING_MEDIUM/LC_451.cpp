// LEETCODE PROBLEM NUMBER 451 - SORT CHARACTERS BY FREQUENCY 


// IN THIS PROBLEM WE WILL FOLLOW THE GIVEN STEPS:

// 1) MAKE A FREQUENCY MAP 
// 2) STORE THE FREQUNECY PAIR IN A VECTOR PAIR 
// 3) SORT THE VECTOR PAIR 
// 4) PUSH THE VECTOR IN THE RESULTANT STRING  



class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char , int>mp;
        vector<pair<char , int>>vec;
        string ans;
        for(auto it : s)
        {
            mp[it]++;
        }
        for(auto it : mp)
        {
            vec.push_back(it);
        }
        sort(vec.begin() ,vec.end() , [](auto a , auto b)
        {
            return a.second>b.second;
        }
        );

        for(auto x : vec)
        {
            ans.append(x.second, x.first);
        }

        return ans ;
    }
};