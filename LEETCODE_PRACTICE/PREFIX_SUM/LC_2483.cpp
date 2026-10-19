// LEETCODE PROBLEM NUMBER 2483 - MINIMUM PENALTY FOR A SHOP 



//APPROACH NUMBER 1 WHICH USES O(n) SPACE AND TIME COMPLEXITY
#include<bits/stdc++.h>
using namespace std ;
class Solution 
{
    public:
          int minimumPenalty(string customers)
          {
            int n = customers.length();
            int minPen = INT_MAX;
            int hour = 0;
            vector<int> prefixN(n + 1, 0);
            vector<int> suffixY(n + 1, 0);

            // Prefix count of N
            for (int i = 1; i <= n; i++) {
                if (customers[i - 1] == 'N') {
                    prefixN[i] = prefixN[i - 1] + 1;
                } else {
                    prefixN[i] = prefixN[i - 1];
                }
            }

            // Suffix count of Y
            for (int i = n - 1; i >= 0; i--) {
                if (customers[i] == 'Y') {
                    suffixY[i] = suffixY[i + 1] + 1;
                } else {
                    suffixY[i] = suffixY[i + 1];
                }
            }

            // Check every possible closing time, including n
            for (int i = 0; i <= n; i++) {
                int current_pen = prefixN[i] + suffixY[i];

                if (current_pen < minPen) {
                    minPen = current_pen;
                    hour = i;
                }
            }
            return hour;
    }
};
int main()
{
    string customer;
    cout<<"ENTER THE STRING :";
    cin>>customer;
    Solution sol;
    cout<<sol.minimumPenalty(customer);
}



//APPROACH NUMBER 2 - WHICH USES O(1) SPACE COMPLEXITY 


#include<bits/stdc++.h>
using namespace std ;
class Solution 
{
    public:
          int minimumPenalty(string customers)
          {
            int n=customers.length();
        int hours=0;
        int penalty=count(begin(customers),end(customers),'Y'); //penalty is the number of customers with 'Y'
        int minimum_penalty=penalty;  //considering total penalty as the minimum penalty
        for(int i=0;i<n;i++)
        {
            if(customers[i]=='Y')
            {
                penalty--;
            }
            else
            {
                penalty++;
            }
            if(penalty<minimum_penalty)
            {   
                minimum_penalty=penalty;
                hours=i+1;
            }   
        }
            return hours;
          }  
    };

int main()
{
    string customer;
    cout<<"ENTER THE STRING :";
    cin>>customer;
    Solution sol;
    cout<<sol.minimumPenalty(customer);
}