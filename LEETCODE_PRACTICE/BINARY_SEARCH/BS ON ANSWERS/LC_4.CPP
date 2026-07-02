// LEETCODE PROBLEM NUMBER 04 - MEDIAN OF TWO SORTED ARRAY 

// APPROACH NUMBER 1 --  THE BRUTE FORCE APPROACH


// IN THIS APPROACH WE HAVE CREATED A HELPER FUNCTION THAT IS USED TO MERGE AND SORT THE TWO GIVEN ARRAYS 
 // AND THEN IN THE MAIN FUNCTION WE CALCULATE THE MEDIAN USING THE FORMULAES OF MEDIAN FOR ODD AND EVEN .

 // TIME COMPLEXITY - O (M+N)
 //SPACE COMPLEXITY -  O(M+N)
 //IT IS NOT A OPTIMAL APPROACH 


 class Solution {
public:
    vector<int> MergedArray(vector<int>& nums1, vector<int>& nums2)
{
    int n = nums1.size();
    int m = nums2.size();
    vector<int> merged_array;
    int i = 0, j = 0;
    while(i < n && j < m)
    {
        if(nums1[i] <= nums2[j])
        {
            merged_array.push_back(nums1[i]);
            i++;
        }
        else
        {
            merged_array.push_back(nums2[j]);
            j++;
        }
    }
    while(i < n)
    {
        merged_array.push_back(nums1[i]);
        i++;
    }
    while(j < m)
    {
        merged_array.push_back(nums2[j]);
        j++;
    }
    return merged_array;
}
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        double median;
        vector<int> merged = MergedArray(nums1, nums2);
        int final_size=merged.size();
        if(final_size%2!=0)
        {
            median= merged[final_size/2];

        }
        else 
        {
            median=(merged[final_size / 2 - 1] + merged[final_size / 2]) / 2.0;
        }
        return median ; 
    }
};