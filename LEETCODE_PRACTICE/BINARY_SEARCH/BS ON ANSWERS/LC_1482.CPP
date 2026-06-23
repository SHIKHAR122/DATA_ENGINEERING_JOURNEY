//LEETCODE PROBLEM NUMBER 1482 - MINIMUM NUMBER OF DAYS TO MAKE m BOUQUETS 

class Solution {
public:
    int findMax(vector<int>& bloomDay)
    {
        int mx = INT_MIN;
        for(int i = 0; i < bloomDay.size(); i++)
        {
            mx = max(mx, bloomDay[i]);
        }
        return mx;
    }

    int countBouquets(vector<int>& bloomDay, int day, int k)
    {
        int bouquets = 0;
        int consecutiveFlowers = 0;

        for(int i = 0; i < bloomDay.size(); i++)
        {
            if(bloomDay[i] <= day)
            {
                consecutiveFlowers++;
            }
            else
            {
                bouquets += consecutiveFlowers / k;
                consecutiveFlowers = 0;
            }
        }

        bouquets += consecutiveFlowers / k;
        return bouquets;
    }

    int minDays(vector<int>& bloomDay, int m, int k) {
        long long requiredFlowers = 1LL * m * k;

        if(requiredFlowers > bloomDay.size())
        {
            return -1;
        }

        int low = 1;
        int high = findMax(bloomDay);
        int ans = -1;

        while(low <= high)
        {
            int mid = low + (high - low) / 2;

            int bouquets = countBouquets(bloomDay, mid, k);

            if(bouquets >= m)
            {
                ans = mid;
                high = mid - 1;
            }
            else
            {
                low = mid + 1;
            }
        }

        return ans;
    }
};