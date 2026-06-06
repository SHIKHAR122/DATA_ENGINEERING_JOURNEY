//LEETCODE PROBLEM NUMBER 54 - SPIRAL MATRIX 
// IN THIS QUESTION WE WILL HAVE 4 POINTERS LEFT , RIGHT  , TOP , BOTTOM THAT IS USED TO MARK THE POSITIONS OF THE MATRIX AND 
//UISNG THOSE POINTERS WE WILL PRINT THE WHOLE 2D MATRIX IN THE 1D VECTOR 
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int>res;
        int n=matrix[0].size();
        int m =matrix.size();
        int left=0;
        int top=0;
        int right=n-1;
        int bottom = m-1;
        while(top<=bottom && left<=right)
        {
            for(int i =left ; i<=right;i++)
            {
                res.push_back(matrix[top][i]);

            }
            top++;
            for(int i=top;i<=bottom;i++)
            {
                res.push_back(matrix[i][right]);
            }
            right--;
            if(top<=bottom)
            {
                for(int i =right;i>=left;i--)
                {
                    res.push_back(matrix[bottom][i]);
                }   
                bottom--;
                
            }
            if(left<=right)
            {
                for(int i =bottom; i>=top;i--)
                {   
                    res.push_back(matrix[i][left]);
                }
                left++;
            }
        }
        return res;
    }
};