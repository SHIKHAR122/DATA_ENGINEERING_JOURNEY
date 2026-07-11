//LEETCODE PROBLEM NUMBER 378 - Kth SMALLESTY ELEMENT IN THE SORTED MATRIX 



//APPROACH NUMBER 1 - THE BRUTE FORCE APPROACH , IN THIS APPROACH WE WILL FLATTEN THE ARRAY FIRST  , 
// AND THEN SORT IT , THEN RETURN THE ARR[k-1] ELEMENT 


//COMPLEXITY OF THE APPROACH IS O (N^2 LOG N )

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        vector<int>res;
        int m = matrix.size();
        int n = matrix[0].size();
        for(int i =0 ;i<m ; i++)
        {
            for(int j  =0 ;j < n ; j++)
            {
                res.push_back(matrix[i][j]);
            }
        }
        sort(res.begin() , res.end());
        return res[k-1];
    }
};




// APPROACH NUMBER 2 - THE BINARY SEARCH APPROACH 
// Binary search on the value range to find the smallest value that has at least k elements less than or equal to it.



// COMPLEXITY OF THIS CODE IS - O (n^2 (max-min))
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int m=matrix.size();
        int n =matrix[0].size();
        int low=matrix[0][0];
        int high=matrix[m-1][n-1];
        int ans=0;
        while(low<=high)
{
            int mid=low+(high-low)/2;
            int count=0;
        for (int i = 0; i < matrix.size(); i++)
{
            for(int j=0;j<matrix[0].size();j++)
{
                if(matrix[i][j]<=mid)
{
                count++;
}
}
}
        if(count<k)
            {
                low=mid+1;
            }
            else 
            {
                ans=mid;
                high=mid-1;
            }
}
        return ans;
}
};





