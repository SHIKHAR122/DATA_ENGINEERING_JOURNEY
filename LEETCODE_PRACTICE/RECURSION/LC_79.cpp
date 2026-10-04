// LEET CODE PROBLEM NUMBER 79  - WORD SEARCH 
// THIS QUESTION WILL BE SOLVED USING THE DFS + GRID + BACKTRACKING APPROACH 



#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
        vector<vector<int>>directions={    //THIS IS THE VECTOR OF THE DIRECTIONS IN WHICH WE CAN MOVE , HAVE THE POSSIBLE MOVES
            {1,0} , //down
            {-1,0}  , //up
            {0,1} , //left
            {0,-1}   //right
        };
          bool findWord(vector<vector<char>>& board, string word,int i , int j , int index )
          {
                int m =board.size();
                int n=board[0].size();
                if(index==word.length())  //if the size of the index matches with the word to be searched then that means the word is found 
                {
                    return true;
                }
                if(i<0||j<0||i>=m||j>=n||board[i][j]=='$')  //if the bounds of the matrix is not followed we will return false or if the word is visited in the grid we return false
                {
                    return false;
                }
                if(board[i][j]!=word[index]) //if the word given is not found in the matrix , then also we will return back
                {
                    return false;
                }
                char temp=board[i][j];   //STORING THE CURRENT WORD IN A TEMPORARY VARIABLE SO THAT AFTER VALIDATING IT WE CAN RE-WRITE THE WORD
                board[i][j]='$';  //OVER WRITING THE VISITED LETTERS SO THAT WE DONT WORK ON THEM 

                for(auto & dir : directions)
                {   
                    int new_i=i+dir[0];    //NEW NEIGHBOURS WHICH WILL BE CHECKED 
                    int new_j=j+dir[1];
                    if(findWord(board,word,new_i,new_j,index+1))    //APPLYING THE RECURSIVE CALL FOR THE NEW INDEXES , IF THEY EXIST THEN WE GET TRUE
                    {
                        return true;
                    }
                }
                board[i][j]=temp;
                return false;
          }
          bool exist(vector<vector<char>>& board, string word)
    {
        int m = board.size();
        int n = board[0].size();

        // Check every cell as a potential starting position
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            { 
                if (board[i][j] == word[0] && findWord(board, word, i, j, 0))    //CHECKING IF THE CURRENT LETTER MATCHES WITH THE WORDS FIRST LETTER , AND ALSO FINDWORD() CHECKS IF FOR THESE INDEXES WE ARE GETTING THE REQUIRED WORD OR NOT 
                {
                    return true;
                }
            }
        }
        return false;
    }
};

int main()
{
    vector<vector<char>> board = {
        {'A', 'B', 'C', 'E'},
        {'S', 'F', 'C', 'S'},
        {'A', 'D', 'E', 'E'}
    };
     string word="SEE";
    Solution sol;
    bool res = sol.exist(board, word);
    cout<<(res?"true":"false")<<endl;
    return 0;
}