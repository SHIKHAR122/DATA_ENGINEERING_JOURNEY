// LEETCODE PROBLEM NUMBER - 39 - COUNT AND SAY ()


#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
            string cas(int n)
            {
                if(n==1){
                    return "1";
                }
                string str= cas(n-1);
                int freq=1;   //this keeps a count of the matching elements of the string , or u can say it store the frequency
                char current= str[0];   //this is the first element of the string
                string ans="";  //this will store the final string which will be returned....
                for(int i=1;i<str.size();i++)   //looping will start from the second element of the string
                {
                    char second = str[i];  //this stores the elements after the first element  for example if the string is "3322251" it will store elements like "3222..."
                    if(current==second)   //if the first and the second element of th e string matches then we will increase the count of the frequency ...
                    {
                        freq++;
                    }
                    else{   //if the first and the current element of the string dont match with each other we will not increase the count , rather we will append the current element along with its frequency 
                            // in the resultant string
                            ans+=to_string(freq)+current;
                            freq=1;  //reset the frequency as from here onwards the string's next elements will be checked ...
                            current=second;   //now the current element is the second element which has broken the frequency streak of the current string ,for example if we had "3322251"
                            //  as soon as we reach the first "2"  , we will break the frequency count of "3" and reset the current pointer to "2" and then start counting the frequnecy of "2"
                    }
                }
                         ans+=to_string(freq)+current;  //here we are appending the left over elements of the string.
                         return ans;
            }
};
int main()
{
    Solution sol;
    string s=sol.cas(4);
    cout<<s;
}