// LEETCODE PROBLEM NUMBER 904 - FRUITS INTO BASKET 

// THIS IS A SLIDING WINDOW PROBLEM WHERE THE WINDOW USED IS A VARIABLE SIZED WINDOW , WHICH MEANS THAT WE KEEP EXPANDING THE WINDOW UNTIL WE GET AN INVALID CONDITION 



#include<bits/stdc++.h>
using namespace std;

class Solution 
{
    public: 
           int totalFruit(vector<int>& fruits) {
        int n=fruits.size();
        int left=0; // the left pointer
        int right=0;  //the right pointer 
        int len=0;  //used to store the current length
        int maxlen=0;   //for storing the max length 
        unordered_map<int , int>freq;
        while(right<n)   
        {
            freq[fruits[right]]++;  //increasing the freq of the right element
            while(freq.size()>2){  //if the size of the map is greater than 2 that means a new element has been introduced in the map which is violating the problems conditiona as the condition only ask for 2 distinct elements in the map 
                freq[fruits[left]]--;  //removing the left element's freq from the map
                if(freq[fruits[left]]==0)  //if that element(left) freq becomes 0 so simply remove it 
                {
                    freq.erase(fruits[left]);//erase that elements existence from the map
                }
                left++; //move the left pointer 
            }   
            len=right-left+1;
            maxlen=max(maxlen , len);
            right++;
        }
        return maxlen;
    }
};

int main ()
{
    Solution sol;
    vector<int>fruits={1,2,3,2,2};
    cout<<sol.totalFruit(fruits);
}