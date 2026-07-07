//LEETCODE PROBLEM NUMBER 240 - SEARCH IN A 2D MATRIX


// THIS IS THE BRUTE FORCE APPROACH FOR THIS PROBLEM
//IN THIS APPROACH WE TREAT EACH ROW OF THE 2D ARRAY AS A 1D ARRAY AND PERFOMR BINARY SEARCH IN EACH OF THEM UNTIL WE GET THE RESULT 




class Solution {
public:
    bool binary_search(vector<int>&result , int target)
    {   
        int low=0;
        int high= result.size()-1;
        while(low<=high)
        {
            int mid = low + (high-low)/2;
            if(result[mid]==target)
            {
                return true;
            }
            else if(result[mid]<target)
            {
                low=mid+1;
            }
            else {
                high=mid-1;
            }
        }
        return false;
    }
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for(int i =0;i < matrix.size();i++)
        {   
            if(binary_search(matrix[i],target))
            {
                return true;
            }
        }
         return false;
    }
   
};