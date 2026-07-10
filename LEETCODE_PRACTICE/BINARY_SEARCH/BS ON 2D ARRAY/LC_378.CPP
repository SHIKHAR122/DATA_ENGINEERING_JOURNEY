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






