// PROBLEM- SUBSETS 

#include<bits/stdc++.h>

using namespace std;

class Solution 
{
    public:
          void subsets(string ans , string og , bool flag)
          {
             if(og=="")
             {
                cout<<ans<<endl;
                return ;
             }
             char ch = og[0];    //first character of the string 
             if(og.size()==1)        //if the size of the string is 1 
             {
                if(flag==true) subsets(ans+ch,og.substr(1), true);
                subsets(ans, og.substr(1) , true);
                return;
             }
             char dh=og[1];   //second character of the string   
             if(ch==dh) //if the first and the next element of the string matches then we will use this condition 
             {  
                if(flag==true)subsets(ans+ch , og.substr(1) , true);
                subsets(ans , og.substr(1) , false);
             }
             else{    //if the first and the second element of the string dont match and the size of the string is > 1
                    if(flag==true)subsets(ans+ch , og.substr(1) , true);
                    subsets(ans , og.substr(1) , true);
             }
          }
};
int main()
{
    Solution sol ;
    string og= "aba";
    sort(og.begin() ,og.end());
    sol.subsets("" , og , true);
}