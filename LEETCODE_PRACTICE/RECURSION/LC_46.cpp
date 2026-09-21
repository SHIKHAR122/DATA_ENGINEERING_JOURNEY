// LEETCODE PROBLEM NUMBER 46  - PERMUTATIONS 

// IN THIS QUESTION WE HAVE TO PRINT ALL THE POSSIBLE  PERMUTATIONS OF THE GIVEN ELEMENTS IN THE ARRAY .

// At every recursive call, choose one element from the current vector and add it to current.
// Create a new vector containing all elements except the chosen element, and recursively generate permutations from it.
// When no elements remain, store the generated permutation in ans; then backtrack and try the next element.


class Solution {
public:
    void permutations(vector<vector<int>>&ans , vector<int>&nums , vector<int>current , int size)
    {   
        if(size==0)
        {
            ans.push_back(current);
            return;
        }
        for(int i=0;i<size;i++)
        {
            
            vector<int>remaining;
            for(int j=0;j<nums.size();j++)
            {
                if(j!=i)
                {
                    remaining.push_back(nums[j]);
                }
            }
            current.push_back(nums[i]);
            permutations(ans , remaining , current , size-1);
            current.pop_back();
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        int n=nums.size();
        vector<vector<int>>ans;
        vector<int>current;
        permutations(ans , nums , current , n);
        return ans ;
    }
};