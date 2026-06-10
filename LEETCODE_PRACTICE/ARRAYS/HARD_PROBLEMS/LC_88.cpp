// LEETCODE PRONLEM NUMBER 88 - MERGE SORTED ARRAYS 

// THIS PROBLEM ALSO HAS MULTIPLE SOLUTIOND 



//APPROACH 1  --  GAP METHOD 
class Solution {
private:
    void swapThem(vector<int>& nums1, vector<int>& nums2, int i1, int i2)
    {
        if(nums1[i1] > nums2[i2])
        {
            swap(nums1[i1], nums2[i2]);
        }
    }

public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n)
    {
        int len = m + n;
        int gap = (len / 2) + (len % 2);

        while(gap > 0)
        {
            int left = 0;
            int right = left + gap;

            while(right < len)
            {
                // nums1 and nums2
                if(left < m && right >= m)
                {
                    swapThem(nums1, nums2, left, right - m);
                }

                // nums2 and nums2
                else if(left >= m)
                {
                    if(nums2[left - m] > nums2[right - m])
                    {
                        swap(nums2[left - m], nums2[right - m]);
                    }
                }

                // nums1 and nums1
                else
                {
                    if(nums1[left] > nums1[right])
                    {
                        swap(nums1[left], nums1[right]);
                    }
                }

                left++;
                right++;
            }

            if(gap == 1)
                break;

            gap = (gap / 2) + (gap % 2);
        }

        for(int i = 0; i < n; i++)
        {
            nums1[m + i] = nums2[i];
        }
    }
};

//Time: O((m+n) log(m+n))
//Space: O(1)






//APPROACH NUMBER 2 - THREE POINTERS 

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i=m-1;
        int j= n-1;
        int k =m+n-1;
        while(i>=0 && j>=0)
        {
            if(nums1[i]>nums2[j])
            {
                nums1[k]=nums1[i];
                i--;
                k--;
            }
            else 
            {
                nums1[k]=nums2[j];
                j--;
                k--;
            }
        }
            while(j>=0)
            {
                nums1[k]=nums2[j];
                k--;
                j--;
            }
        
    }
};