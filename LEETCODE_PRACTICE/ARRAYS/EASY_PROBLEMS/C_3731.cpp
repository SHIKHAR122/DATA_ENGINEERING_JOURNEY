// LEETCODE PROBLEM NUMBER 3731 - FIND MISSING ELEMENTS 


//IN THIS PROBLEM , THE APPROACH CAN BE TO FIND THE MAXIMUM AND MINIMUM RANGE OF THE ARRAY , TRAVERSE IN IT 
// AND THEN  WHILE TRAVERSING IF THE ELEMENT IS NOT FOUND IN THE ORIGINAL VECTOR ,PUSH THAT ELEMENT IN THE RESULT VECTOR 




class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
        int mn = *min_element(nums.begin(),nums.end());
        int mx = *max_element(nums.begin(),nums.end());
        int n=nums.size();
        vector<int>ans;
        for(int i=mn;i<=mx;i++)
        {
            auto it =find(nums.begin() , nums.end() , i);
            if(it==nums.end())
            {
                ans.push_back(i);
            }
        }
        return ans ;
    }
};