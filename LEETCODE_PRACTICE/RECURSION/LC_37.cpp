// LEETCODE PROBLEM NUMBER 37 - SUDOKU SOLVER 
// THE FOLLOWING QUESTION IS OF THE PATTERN -GRID FILLING BACKTRACKING 
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isSafe(int row, int col, vector<vector<char>>& board, char num)
    {
        for (int i = 0; i < 9; i++)
        {
            // Check row
            if (board[row][i] == num)
                return false;

            // Check column
            if (board[i][col] == num)
                return false;

            // Check 3x3 sub-box
            if (board[3 * (row / 3) + i / 3]
                     [3 * (col / 3) + i % 3] == num)
                return false;
        }

        return true;
    }

    bool placeNum(vector<vector<char>>& board)
    {
        for (int row = 0; row < 9; row++)
        {
            for (int col = 0; col < 9; col++)
            {
                if (board[row][col] == '.')
                {
                    for (char num = '1'; num <= '9'; num++)
                    {
                        if (isSafe(row, col, board, num))
                        {
                            board[row][col] = num;

                            if (placeNum(board))
                                return true;

                            // Backtrack
                            board[row][col] = '.';
                        }
                    }

                    return false;
                }
            }
        }

        return true;
    }

    void solveSudoku(vector<vector<char>>& board)
    {
        placeNum(board);
    }
};

int main()
{
    Solution sol;

    vector<vector<char>> board = {
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}
    };

    sol.solveSudoku(board);

    // Print the solved Sudoku
    for (int row = 0; row < 9; row++)
    {
        for (int col = 0; col < 9; col++)
        {
            cout << board[row][col] << " ";
        }
        cout << endl;
    }

    return 0;
}