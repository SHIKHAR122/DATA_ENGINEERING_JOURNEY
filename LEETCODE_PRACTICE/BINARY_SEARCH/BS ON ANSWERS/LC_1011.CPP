// LEETCODE PROBLEM NUMBER - 1011 CAPACITY TO SHIP PACKAGES WITHIN "D" DAYS 
// THIS PROBLEM IS SOLVED USING THE CONCEPT OF BINARY SEARCH ON ANSWERS



class Solution {
public:
    int countDay(vector<int>&weights , int capacity)
    {
        int load=0;
        int day =1;
        for(int i =0 ; i<weights.size();i++)
        {
            if(weights[i]+load > capacity)
            {
                day++;
                load=weights[i];
            }
            else {
                load+=weights[i];
            }
        }
        return day ;
    }
    int shipWithinDays(vector<int>& weights, int days) {
        int low= *max_element(weights.begin(),weights.end());
        int high=accumulate(weights.begin(), weights.end(),0);
        while(low<=high)
        {
            int mid=low+(high-low)/2;
            int day = countDay(weights,mid);
            if(day<=days)
            {
                high=mid-1;
            }
            else{
                low=mid+1;
            }
        }
        return low; 
    }
};