//LEETCODE PROBLEM NUMBER 74 - SEARCH IN 2D MATRIX 


//APPROACH NUMBER 1   - BRUTE FORCE
// IN THIS APPROACH WE HAVE FLATTEN THE 2D MATRIX BY SIMPLY CONVERTING IT INTO A 1D MATRIX AND THEN APPLYING BINARY SEARCH 

// THE TIME COMPLEXITY IS -    AND THE SPACE COMPLEXITY IS - O(M*N)


class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        vector<int>arr;
        for(int i=0 ; i<matrix.size();i++)
        {
            for(int j =0;j<matrix[0].size();j++)
            {
                arr.push_back(matrix[i][j]);
            }
        }
        int low=0;
        int high=arr.size()-1;
        while(low<=high)
        {
            int mid=low+(high-low)/2;
            if(target==arr[mid])
            {
                return true;
            }
            else if(arr[mid]<target){
                low=mid+1;
            }   
            else{
                high=mid-1;
            }
        }
        return false;
    }
};






//APPROACH NUMBER 2 
// OPTIMAL APPROACH FOR LC 74 - 
//COMPLEXITY IS O(LOG(M*N))

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    int low = 0;
    int high = rows * cols - 1;

    while(low <= high)
    {
        int mid = low + (high - low) / 2;

        int row = mid / cols;
        int col = mid % cols;

        if(matrix[row][col] == target)
            return true;
        else if(matrix[row][col] < target)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return false;
    }
};