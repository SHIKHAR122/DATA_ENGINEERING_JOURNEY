// LEETCODE PROBLEM NUMBER 2389- LONGEST SUBSEQUENCE WITH LIMITED SUM 

//TIME COMPLEXITY OF THIS CODE IS - O(n(m+log n )) ~= O(m*n)
//SPACE COMPLEXITY OF THIS CODE IS - O(log n)
// sort the vector first , then within the given vector calculate its prefix sum 
// after calculating the prefix sum simply traverse the queries vector and the prefixsum vector 
// and for each element check whether the given sum is less than or equal to the queries[i] , if it is smaller then keep increasing the length  of the subsequence
// other wise break


#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        int n=nums.size();
        int m=queries.size();
        vector<int>answer(m);
        sort(nums.begin() , nums.end());
        //make prefix sum
        for(int i=1;i<n;i++)
        {
            nums[i]=nums[i-1]+nums[i];
        }
        for(int i=0;i<m;i++)  //loop for answer  vector
        {
            int len=0;
            for(int j=0;j<n;j++)   //loop for nums vector
            {
                if(nums[j]>queries[i]) break;//if the current prefix sum in the nums is greater than the queries[i] then we will simply break kyunki humein queries se chota yaa uske barabar ka subsequence sum chaiye naa ki usse bda 
                len++;//if upr wali condition false h toh simply length bda denge
            }
            answer[i]=len; //store that length in the answer vector 
        }
        return answer;
    }
};
int main()
{
    Solution sol;
    vector<int> nums={4,5,2,1};
    vector<int>queries={3,10,21};
    vector<int>answer=sol.answerQueries(nums , queries);
    for(int i=0;i<n;i++){
        cout<<answer[i];
    }
}




// THE OPTIMAL APPROACH TO SOLVE THIS PROBLEM IS TO USE BINARY SEARCH RATHER THAN USING THE LINEAR SEARCH , WHICH WAS COSTING US TIME COMPLEXITY 
//  SO THE CODE FOR THE OPTIMAL APPRPOACH IS : 

#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        int n=nums.size();
        int m=queries.size();
        vector<int>answer(m);
        sort(nums.begin() , nums.end());
        //make prefix sum
        for(int i=1;i<n;i++)
        {
            nums[i]=nums[i-1]+nums[i];
        }
        for(int i=0;i<m;i++)  //loop for answer  vector
        {
            int len=0;
            //binary search instead of for loops (reducing time complexity)
            int low=0;
            int high=n-1;
            while(low<=high)
            {
                int mid=low+(high-low)/2;
                if(nums[mid]>queries[i])
                {
                    high=mid-1;
                }
                else //nums[mid]<=queries[i]
                {
                    len=mid+1;
                    low=mid+1;
                }
            }   
            answer[i]=len;
        }
        return answer;
    }
};
int main()
{
    Solution sol;
    vector<int> nums={4,5,2,1};
    vector<int>queries={3,10,21};
    vector<int>answer=sol.answerQueries(nums , queries);
    for(int i=0;i<n;i++){
        cout<<answer[i];
    }
}