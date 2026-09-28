// LEETCODE PROBLEM NUMBER 779 - Kth SYMBOL IN THE GRAMMAR 
// KTH GRAMMAR: Instead of generating the entire row, recursively trace the kth element
// back to the previous row: odd k keeps the previous value, while even k flips it.
// We repeatedly reduce n and k until row 1, whose value is always 0.


#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
            int kthgrammar(int n,int k)
            {   
                if(n==1)return 0;   //this is the base case where the first row always returns 0 

                if(k%2==0)  //if kth element is even then the answer returned will be flipped ans will be found at the k/2th element 
                {
                    int prevAns=kthgrammar(n-1,k/2);
                    if(prevAns==0) return 1;   //flipping the answer
                    else return 0;
                }
                else {  //if the kth element is odd , then the answer returned will not be flippped and will be found at the k/2+1th element
                    int prevAns=kthgrammar(n-1,k/2+1);
                    return prevAns;
                }

            }
};
int main()
{
    Solution sol;
    int n=4;
    int k=4;
    int res=sol.kthgrammar(n,k);
    cout<<res;

}
