#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public:
           int MaxConsecutiveOnes(vector<int>&nums , int k)
           {
                int n = nums.size();
                int i=0;
                int j=0;
                int flip=0;  //counts the number of flips in the array
                int len=0; //stores the length of the window
                int maxlen= INT_MIN;  //stores the maximum length of the window seen so far 
                while(j<n) 
                {   
                    if(nums[j]==1)   //if the number encounteres is a 1 then we will increase the range of the window
                    {
                        j++;
                    }
                    else{  //else if the number encountered turns out to be 0 , then we will simply check if the number of flips done is still less than the number of flips left to do (k) 
                        if(flip<k){

                            flip++; //if the above condition is true , then we will increase the flip count
                            j++;
                        }
                        else{  //nums[j]==0 and the number of flips is equal to the number of k 
                            len=j-i;
                            maxlen=max(maxlen, len);
                            while(nums[i]==1)  //now simply place the i to that index where we encounter our first '0' else we simply keep moving the ith pointer 
                            {
                                i++;    
                            }

                            //now my ith index is 100 % at the index where we have a 0 in the array   nums[i]=0
                            i++;
                            j++;
                        }
                    }
                }
                len=j-i;
                maxlen=max(maxlen, len);
                return maxlen;
           }
};
int main()
{
    Solution sol;
    vector<int>nums;
    int n=nums.size();
    int k;
    cout<<"ENTER THE VALUE OF K : ";
    cin>>k;
    cout<<"ENTER THE ELEMENTS OF THE ARRAY: ";
    for(int i=0;i<n;i++)
    {
        cin>>nums[i];
    }

}