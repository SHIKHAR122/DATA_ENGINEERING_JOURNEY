//LEETCODE PROBLEM NUMBER 1901 - FIND PEAK ELEMENT - II

// APPROACH NUMBER 1 --   BRUTE FORCE APPROACH 

// IN THIS APPROACH WE WILL USE LOOPING FOR ROW AND COLUMNS AND HANDLE THE EDGE CASES AND THEN CHECK EACH ELEMENTS 
// TOP , BOTTOM , RIGHT AND LEFT TO GET THE MAX ELEMENTS ..


//COMPLEXITY OF THIS CODE IS -   O ( M x N ) , WHICH IS NOT THE OPTIMAL APPROACH FOR THIS PROBLEM  
class Solution {
public:
    vector<int> findPeakGrid(vector<vector<int>>& mat) {
        int m = mat.size();
        int n= mat[0].size();
        int up,down,left,right;
        for(int i =0 ;i<m ; i++)
        {
            for(int j =0 ;j<n ; j++)
            {
                if(i>0)
                {
                    up=mat[i-1][j];
                }
                else{
                    up=-1;
                }
                if(i<m-1)
                {
                    down=mat[i+1][j];
                }
                else{
                    down=-1;
                }
                if(j>0)
                {
                    left=mat[i][j-1];
                }
                else{
                    left=-1;
                }
                if(j<n-1)
                {
                    right=mat[i][j+1];
                }
                else{
                    right=-1;
                }
                if (mat[i][j] > up &&
                    mat[i][j] > down &&
                    mat[i][j] > left &&
                    mat[i][j] > right)
                {
                        return {i, j};
                }
            }
        }
        return {};
    }
};





