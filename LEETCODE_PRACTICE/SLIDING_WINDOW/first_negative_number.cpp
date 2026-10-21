// FIRST NEGATIVE NUMBER IN EVERY WINDOW OF THE SIZE 'K'

// BRUTE FORCE APPROACH 
//TIME COMPLEXITY ~= O(n*k)
#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
           vector<int>NegativeNum(vector<int>&nums , int k)
           {
                int n=nums.size();
                vector<int>answer;
                for(int i=0;i<=n-k;i++)  //this loop runs from 0th index to the n-k+1 index
                {
                    int firstneg=0;
                    for(int j=i;j<i+k;j++)    //this is used to create the window for the given size (k)
                    {
                        if(nums[j]<0)   //if the element in the current window is negative then we will simply push it into the array
                        {
                            firstneg=nums[j];
                            break;
                        }
                    }
                    answer.push_back(firstneg);
                }
                return answer;
           }
};

int main()
{
    Solution sol;
    int k=3;
    vector<int>nums={2,-3,4,4,-7,-1,4,2,-6};
   vector<int>answer= sol.NegativeNum(nums , k);
   for(int i=0;i<answer.size();i++)
   {
        cout<<answer[i]<<" ";
   }
}





// OPTIMAL APPROACH IS TO USE THE SLIDING WINDOW 
// TIME COMPLEXITY OF THIS APPROACH WILL BE O(n)



#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
            vector<int>FirstNegativeNum(vector<int>&nums , int k)
            {
                vector<int>answer;  //answer vector to store the negative numbers 
                int n=nums.size();
                int prevnegnum=0;
                //finding the previous negative number 
                for(int i=0;i<k;i++)
                {
                    if(nums[i]<0)
                    {
                        prevnegnum=i;  //if the number is less than 0 then it is negative and hence stored its index  in this variable
                    }

                }
                //applying the sliding window in the given array
                int i=1;
                int j=k;
                while(j<n)
                {
                    if(prevnegnum>=i)  //if the previous negative number is already greater than or equal to the i which is the first element in the sliding window then the prevnegnum is the only valid number in both the windows 
                    {
                        answer[i]=nums[prevnegnum];
                    }
                    else{  //if the above condn. is not true then simply we will traverse till the end of the window and check for the first negative number in that range  
                        for(prevnegnum=i;prevnegnum<j;prevnegnum++)
                        {
                            if(nums[prevnegnum]<0)
                            {
                                break;
                            }
                            answer[i]=nums[prevnegnum];  //storing and updating the position for the previous negative number 
                        }
                    }
                    i++;
                    j++;
                }
                return answer;
            }
};
int main()
{
    Solution sol;   
    vector<int>nums={2,-3,4,4,-7,-1,4,2,-6};
    vector<int>answer= sol.FirstNegativeNum(nums , k);
        for(int i=0;i<answer.size();i++)
        {
            cout<<answer[i]<<" ";
        }
}