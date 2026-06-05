//LEETCODE PROBLEM NUMBER 48 - ROTATE IMAGE 
//IN THIS PROBLEM WE WILL ROTATE THE MATRIX BY SIMPLY TRANSPOSING IT FIRST AND THEN REVERSE THE ROWS
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        for(int i =0;i<matrix.size();i++)
        {
            for(int j =i;j<matrix.size();j++)   
            {
                swap(matrix[i][j],matrix[j][i]);
            }
        }
        for(int i =0;i<matrix.size();i++)
        {
            reverse(matrix[i].begin(),matrix[i].end());
        }
    }
};