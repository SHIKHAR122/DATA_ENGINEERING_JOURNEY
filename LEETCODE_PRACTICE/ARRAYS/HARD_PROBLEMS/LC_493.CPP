// LEETCODE PROBLEM NUMBER 493 - REVERSE PAIRS 

class Solution {
   void merge(vector<int>& nums, int low, int mid, int high)
{
    vector<int> temp;
    int left = low;
    int right = mid + 1;
    while(left <= mid && right <= high)
    {
        if(nums[left] <= nums[right])
        {
            temp.push_back(nums[left++]);
        }
        else
        {
            temp.push_back(nums[right++]);
        }
    }
    while(left <= mid)
        temp.push_back(nums[left++]);
    while(right <= high)
        temp.push_back(nums[right++]);
    for(int i = low; i <= high; i++)
    {
        nums[i] = temp[i - low];
    }
}
    int countpairs(vector<int>& nums, int low, int mid, int high)
    {
    int right = mid + 1;
    int count = 0;
    for(int i = low; i <= mid; i++)
    {
        while(right <= high && nums[i] > 2LL * nums[right])
        {
            right++;
        }
        count += right - (mid + 1);
    }
    return count;
}
    int ms(vector<int>& nums , int low , int high)
    {
        int count=0;
        if(low>=high) return count;
        int mid = (low+high)/2;
        count+=ms(nums,low,mid);
        count+=ms(nums,mid+1,high);
        count += countpairs(nums, low, mid, high);
        merge(nums, low, mid, high);
        return count;
    }
public:
    int reversePairs(vector<int>& nums) {
        return ms(nums,0,nums.size()-1);
    }
};