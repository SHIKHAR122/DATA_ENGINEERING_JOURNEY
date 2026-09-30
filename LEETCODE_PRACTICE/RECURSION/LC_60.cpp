// LEETCODE PROBLEM NUMBER - 60 SEQUENCE PERMUTATIONS 


// APPROACH NUMBER 1 - USING THE BRUTE FORCE  :

// WE WILL CREATE 2 HELPER FUNCTIONS ONE WILL GENERATE STRING TILL 'n' , AND THE OTHER ONE WILL GENERATE ALL THE POSSIBLE PERMUTATIONS TILL THE K ELEMENT  OF THE STRING PASSED TO IT 
// THEN IN THE MAIN FUNCTION WE WILL RETURN THE Kth PERMUTATION .





#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
          string GenerateString(int n)
          {
             string str="";
             for(int i=0;i<n;i++)
             {
                str.append(to_string(i));
             }
             return str;
          }
          string GeneratePerm(string str , int sizes , int &count , string ans , vector<string>&result ,int k )
          {
              if(sizes==0)
              {
                count++;
                if(count==k){
                    result.push_back(ans);
                    return;
                }
                return ;
              }
              for(int i=0;i<str.size();i++)
              {
                  char ch=str[i];
                  string remaining= str.substr(0,i)+str.substr(i+1);
                  GeneratePerm(remaining,sizes-1,count,ans+ch,result,k);
                  if(count==k)
                  {
                    return ;
                  }
              }
          }
};
int main()
{
    int n;
    cout<<"ENTER THE SIZE OF THE STRING";
    cin>>n;
    string ans="";
    Solution sol;
    vector<string>result;
    int count=0;
    int k =5;
    string str=sol.GenerateString(n);
    int sizes=n;
    string res=sol.GeneratePerm(str , sizes , count ,ans , result ,k);
}


// THIS IS NOT AN OPTIMAL APPROACH TO SOLVE THIS PROBLEM 
