// GFG PROBLEM NUMBER 6 - RAT IN A MAZE 
// THIS QUESTION IS SOLVED USING THE - BACKTRACKING + GRID DFS ALGORITHM


#include <bits/stdc++.h>
using namespace std;
class Solution
{
    int dr[4] = {1, 0, 0, -1};
    int dc[4] = {0, -1, 1, 0};
    string directions = "DLRU";
public:
    bool IsValid(int r, int c, int n, vector<vector<int>>& maze)
    {
        return r >= 0 && c >= 0 &&r < n && c < n &&maze[r][c] == 1;
    }

    void findPath(int r, int c,vector<vector<int>>& maze,string& path,vector<string>& res)
    {
        int n = maze.size();
        // Destination reached
        if(r == n - 1 && c == n - 1)
        {
            res.push_back(path);
            return;
        }
        // Mark current cell as visited
        maze[r][c] = 0;
        for(int i = 0; i < 4; i++)
        {
            int new_r = r + dr[i];
            int new_c = c + dc[i];
            if(IsValid(new_r, new_c, n, maze))
            {
                path.push_back(directions[i]);
                findPath(new_r, new_c, maze, path, res);
                path.pop_back();
            }
        }
        // Backtrack: unmark current cell
        maze[r][c] = 1;
    }
    vector<string> RatInMaze(vector<vector<int>>& maze)
    {
        vector<string> res;
        int n = maze.size();
        string path = "";
        if(maze[0][0] == 1 && maze[n - 1][n - 1] == 1)
        {
            findPath(0, 0, maze, path, res);
        }
        sort(res.begin(), res.end());
        return res;
    }
};
int main()
{
    vector<vector<int>> maze = {
        {1, 0, 0, 0},
        {1, 1, 0, 1},
        {1, 1, 0, 0},
        {0, 1, 1, 1}
    };
    Solution sol;
    vector<string> result = sol.RatInMaze(maze);
    for(auto p : result)
    {
        cout << p << " ";
    }
    return 0;
}