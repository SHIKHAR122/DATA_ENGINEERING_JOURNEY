//LEETCODE PROBLME NUMBER - 189 ROTATE ARRAY BY K PLACES 
// FIND THE ACTUAL VALUE OF K  AND THEN FIND THE ROTATION OF THE ARRAY 
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
         k = k % n ;
        reverse(nums.begin(),nums.end());
        reverse(nums.begin(),nums.begin()+k);
        reverse(nums.begin()+k,nums.end());
    }
};