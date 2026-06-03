//LEETCODE PROBLEM NUMBER - 2149 REARRANGE ARRAY ELEMENTS BY SIGN
// THIS PROBLEM CAN BE SOLVED USING TWO APPROACHES


//APPROACH 1 - IN THIS APPROACH WE CAN DEFINE 2 MORE VECTORS WHERE ONE WILL STORE ALL THE POSITIVE TERMS AND THE OTHER WILL STORE NEGATIVE TERMS 
//AND THEN ACCORDING TO THE QUESTION ALL THE POSITIVE VALUES CAN BE STORED IN THE RESULT VECTOR IN EVEN INDEX AND NEGATIVE IN ODD INDEX
class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int n=nums.size();
        vector<int>pos;
        vector<int>neg;
        vector<int>res(n,0);
        int posindex=0;
        int negindex=0;
        for( int num:nums)
        {
            if(num>=0)
            {
                pos.push_back(num);
            }
            else
            {
                neg.push_back(num);
            }
        }
        for(int i=0;i<nums.size();i++)
        {
            if(i%2==0)
            {
                res[i]=pos[posindex++];
            }
            else
            {
                res[i]=neg[negindex++];
            }
        }
        return res;
    }
};

//MORE OPTIMAL APPROACH 
class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int n=nums.size();
        vector<int>res(n,0);
        int posindex=0;
        int negindex=1;
        for(int i=0;i<n;i++)
        {
            if(nums[i]>0)
            {
                res[posindex]=nums[i];
                posindex+=2;
            }
            else
            {
                res[negindex]=nums[i];
                negindex+=2;
            }
        }
        return res;
    }
};