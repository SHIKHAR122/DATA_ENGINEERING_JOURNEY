// LEETCODE PROBLEM NUMBER 51 - N- QUEENS 
//Use backtracking to place one queen per row, check the column and both upper diagonals for safety, recursively explore valid placements, and remove each queen while backtracking to find all solutions.

#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
           bool isSafe(int row , int col , vector<string>&board)  //function to check if the queen can be placed at the given rows and columns 
           {
            int n=board.size();
            for(int i=row-1;i>=0;i--)  //upper direction 
            {   
                if(board[i][col]=='Q')  //here we are checking the upper row , as the column remains the same we wont run 2 loops simply check the ith row which is all the rows above the current row 
                {
                    return false;
                }
            } 
            for(int i = row-1, j = col-1;i >= 0 && j >= 0;i--, j--)
            {
                if(board[i][j]=='Q')
                {
                    return false;
                }
            }
            for(int i=row-1,j=col+1;i>=0&&j<n;i--,j++)           //checking for the upper right diagonal
            {
                   if(board[i][j]=='Q')
                    {
                        return false;
                    }
            }
            return true;        //returning true if the queen is not been attacked at any given coordinates(upper,upper left diagonal and upper right diagonal)
           }

           void PlaceQueens(int n , int row , vector<string>&board , vector<vector<string>>&result)  //this is the recursive function who is responsible for keeping the queens in the desired places 
           {    
                //checking for the base cases 
                if(row>=n)   //if the row passed becomes greater the actual size of the matrix then we will simply return and push back to the final result 
                {   
                    result.push_back(board);
                    return;
                }
                for(int col=0;col<n;col++)
                {
                    if(isSafe(row ,col , board))  //if this function returns true it means that we can place the queen in the given coordinate 
                    {
                        board[row][col]='Q';
                        PlaceQueens(n,row+1,board,result);
                        board[row][col]='.'; //resetting the value if the board is not safe to place the queen , then write  '.' as its default value 
                }
           }
        }

           vector<vector<string>> solveNQueens(int n)
        {
            vector<string> board(n, string(n, '.'));
            vector<vector<string>> result;
            PlaceQueens(n, 0, board , result);
            return result;
        }

};
int main()
{
    Solution sol;
    vector<vector<string>> ans = sol.solveNQueens(4);
    for(auto board : ans)
    {
        for(auto row : board)
        {
            cout << row << endl;
        }
        cout << endl;
    }
}