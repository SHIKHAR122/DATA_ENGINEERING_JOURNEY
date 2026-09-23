// GFG PROBLEM - SUBSEQUENCE WITH SUM K 


// THIS PROBLEM WILL BE SOLVED USING THE RECURSIVE APPROACH  , WHERE WE WILL BE USING THE "TAKE / NOT TAKE" APPROACH-

// 1) FIRST RECURSIVE CALL WILL BE "TAKE" WHICH MEANS THAT WE WILL INCLUDE THE CURRENT ELEMENT IN THE SUM 
// 2) SECOND RECURSIVE CALL WILL BE "NOT TAKE" WHICH MEANS THAT WE WILL NOT INCLUDE THE CURRENT ELEMENT IN THE SUM .


#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        bool subs(vector<int>&arr , int k , int sum , int index)
          {
            int n=arr.size();
             if(index==n)
             return sum==k;    //base case

            bool take= subs(arr , k , sum+arr[index] , index+1);
            bool nottake= subs(arr , k , sum , index+1);
             return take||nottake;
          }

};
int main()
{
    Solution sol;
    vector<int>arr{10,1,2,7,6,1,5};
   cout<< sol.subs(arr ,8 , 0 ,0);
}


// TIME COMPLEXITY FOR THIS CODE WILL BE O(2^N)