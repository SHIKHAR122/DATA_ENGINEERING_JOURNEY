// LEETCODE PROBLEM NUMBER 1539 - Kth MISSING POSITIVE NUMBER 

//THE FIRST APPROACH IS DONE USING THE BRUTE FORCE 
// IN THIS APPROACH WE HAVE TAKEN ANOTHER ARRAY OF THE SIZE max(arr)+k size and then traverse that array 
//and flagged each element with a count of 1 , if the count reaches "k" THEN THE EQUIVALENT ELEMENT IS RETURNED

// COMPLEXITY OF THE CODE IS O( n * (n+k))   --NOT AN OPTIMAL SOLUTION 

class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int count=0;
        int maxi=INT_MIN;
        int res;
        for(int i =0 ;i <arr.size();i++)
        {
            maxi=max(maxi,arr[i]);
        }
        vector<int>searchspace(maxi+k);
        for(int i = 0; i <searchspace.size() ; i++)
        {
            searchspace[i] = i + 1;
        }
        for(int i =0 ;i<searchspace.size();i++)
        {
            if(find(arr.begin(), arr.end(), searchspace[i]) == arr.end())
            {
                count++;
                if(count==k)
                {
                    res=searchspace[i];
                }
            }
        }
        return res;

    }
};