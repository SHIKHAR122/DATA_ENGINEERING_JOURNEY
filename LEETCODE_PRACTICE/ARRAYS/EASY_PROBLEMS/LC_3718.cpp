// LEETCODE PROBLEM NUMBER 3718  - SMALLEST MISSING MULTIPLE OF K 

// APPROACH NUMBER 1 - IN THIS APPROACH WE WILL Start from k → check whether it exists → if it exists, move to the next multiple → stop at the first missing multiple.
class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) {
        int multiple = k;

        while (find(nums.begin(), nums.end(), multiple) != nums.end())
        {
            multiple += k;
        }

        return multiple;
    }
};




// APPROACH NUMBER 2 - THE SAME LOGIC BUT IMPLEMENTED UISNG THE HASH SET
class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) {
        unordered_set<int>st(nums.begin() , nums.end());
        int multiple=k;
        while(st.count(multiple))
        {
            multiple+=k;
        }
        return multiple;
    }
};