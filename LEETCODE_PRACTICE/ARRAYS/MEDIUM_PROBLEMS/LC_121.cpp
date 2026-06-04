// LEETCODE PROBLEM NUMBER 121 - BEST TIME TO BUY AND SELL STOCKS 
//THIS QUESTION CAN HAVE TWO SOLUTIONS 
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int current=nums[0];
        int max_sum=nums[0];
        for(int i=1;i<nums.size();i++)
        {
            current=max(nums[i],current+nums[i]);
            max_sum=max(max_sum,current);
        }
        return max_sum;
    }
};


//ANOTHER APPROACH IS - 
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buyprice=prices[0];
        int profit=0;
       
        for(int i=1;i<prices.size();i++)
        {
            if(buyprice>prices[i])
            {
                buyprice=prices[i];
                
            }
            profit=max(profit,prices[i]-buyprice);
        }
        return profit;
    }
};  //THIS APPROACH IS MORE OPTIMAL AS IT WORKS WITH THE COMPLEXITY - O(N)