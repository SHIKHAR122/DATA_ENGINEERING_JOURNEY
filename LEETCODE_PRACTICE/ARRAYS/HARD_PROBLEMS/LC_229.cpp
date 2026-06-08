// LEETCODE PROBLEM NUMBER 229 - MAJORITY ELEMENTS - II
//IN THIS PROBLEM WE WILL AGAIN USE THE MOORE'S VOTING ALGORITHM AND ELIMINATE THE ELEMENT WITH LESS COUNT AND PUSH THE RESULT IN THE OTHER VECTOR 
// AND RETURN IT 


class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n =nums.size();
        int c1=INT_MIN;
        int c2=INT_MIN;
        int count1=0;
        int count2=0;
        int threshold=n/3;
        vector<int>result;
        for(int i =0;i<n;i++)
        {
            if(nums[i]==c1)
            {
                count1++;
            }
            else if(nums[i]==c2)
            {
                count2++;
            }
            else if(count1==0)
            {
                c1=nums[i];
                count1++;
            }
            else if(count2==0)
            {
                c2=nums[i];
                count2++;
            }
            else
            {
                count1--;
                count2--;
            }
        }
        count1=0;
        count2=0;
        for(int i =0; i<n ; i++)
        {
            if(nums[i]==c1)
            {
                count1++;
            }
            else if(nums[i]==c2)
            {
                count2++;
            }
        }
        if(threshold<count1) result.push_back(c1);
        if(threshold<count2) result.push_back(c2);
        return result;
    }
};