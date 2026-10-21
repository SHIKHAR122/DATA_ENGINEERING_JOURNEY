// LEETCODE PROBLEM NUMBER 1052  - GRUMPY BOOKSTORE OWNER 

#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
          int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        int prevloss=0;
        int maxloss=0;
        int k=minutes;
        int n=customers.size();
        for(int i=0;i<k;i++)
        {   
            if(grumpy[i]==1) prevloss+=customers[i];
        }   
        maxloss=prevloss;
        int maxindex=0;
        int i=1;
        int j=k;
        while(j<n)
        {
            int currentloss=prevloss;
            if(grumpy[j]==1) currentloss+=customers[j];
            if(grumpy[i-1]==1)currentloss-=customers[i-1];
            if(currentloss>maxloss)
            {
                maxloss=currentloss;
                maxindex=i;
            }
            prevloss=currentloss;
            i++;
            j++;
        }
        for(int i=maxindex;i<maxindex+k;i++)
        {
            grumpy[i]=0;
        }
        int sum=0;
        for(int i=0;i<n;i++)
        {
            if(grumpy[i]==0)
            {
                sum+=customers[i];
            }
        }
        return sum;
    }
};
int main()
{
    Solution sol;
    vector<int>customers={1,0,1,2,1,1,7,5};
    vector<int>grumpy={0,1,0,1,0,1,0,1};
    int minutes=3;
    int result=sol.maxSatisfied(customers , grumpy , minutes);
    cout<<result;
}