//LEETCODE PROBLEM NUMBER 118 - PASCAL'S TRIANGLE 
// THIS PROBLEM IS SOLVED BY MAKING A HELPER FUNCTION GENERATING ROWS IN THAT FUNCTION BY THE FORMULA- ANS=ANS*(ROW_INDEX-COLUMN_INDEX)/COLUMN_INDEX
// AND THEN RETURNING THE VECTOR TO THE MAIN FUNCTION ...

class Solution {
public:
    vector<int> generateRows(int row)
    {
        long long ans = 1;
        vector<int> ansrow = {1};
        for(int i = 1; i < row; i++)
        {
            ans = ans * (row - i);
            ans = ans / i;
            ansrow.push_back(ans);
        }
        return ansrow;
    }
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle;
        for(int i = 1; i <= numRows; i++)
        {
            triangle.push_back(generateRows(i));
        }
        return triangle;
    }
};