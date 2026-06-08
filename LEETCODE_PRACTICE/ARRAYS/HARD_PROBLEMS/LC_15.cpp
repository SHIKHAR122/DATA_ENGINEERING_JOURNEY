// LEETCODE PROBLEM NUMBER 15 - 3SUM 
// WE CAN SOLVE THIS PROBLEM BY TWO DIFFERENT APPROACHES



//APPROACH NUMBER 1 - 
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>>st;
        int n =nums.size();
        for(int i=0;i<n;i++)
        {
            set<int>hashSet;
            for(int j=i+1;j<n;j++)
            {
                int third=-(nums[i]+nums[j]);
                if(hashSet.find(third)!=hashSet.end())
                {
                    vector<int>temp={nums[i],nums[j],third};
                    sort(nums.begin(),nums.end());
                    st.insert(temp);
                }
                hashSet.insert(nums[j]);
            }
        }
        vector<vector<int>>answer(st.begin(),st.end());
        return answer;
    }
};

//BUT IN THIS APPROACH THE TIME COMPLEXITY IS SOMEWHERE AROUND ~O(N^2 X log M) WHICH IS NOT OPTIMAL SO WE WILL USE THE OPTIMAL APPROACH 


// ==============================================================================================================================================





// IN THIS APPROACH WE ARE FIXING ONE OF THE THREE TERMS AND THEN UISNG THE TWO POINTERS APPROACH TO SOLVE THIS PROBLEM

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n =nums.size();
        vector<vector<int>>result;
        sort(nums.begin(),nums.end());
        for(int i=0;i<n;i++)
        {
            if(i>0 && nums[i]==nums[i-1]) continue;
            int j= i+1;
            int k =n-1;
            
            while(j<k)
            {
                int sum=nums[i]+nums[j]+nums[k];
                if(sum<0)
                {
                    j++;
                }
                else if(sum>0)
                {
                    k--;
                }
                else
                {
                    vector<int>temp={nums[i],nums[j],nums[k]};
                    sort(temp.begin(),temp.end());
                    result.push_back(temp);
                    j++;
                    k--;
                while(j<k && nums[j-1]==nums[j])j++;
                while(j<k && nums[k+1]==nums[k])k--;

                }
            }
        }
        return result;
    }
};
// THIS SOLUTION HAS TIME COMPLEXITY OF ABOUT ~~ O(log N )
