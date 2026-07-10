//  LEETCODE PROBLEM NUMBER 42 - TTRAPPING RAINWATER 



// APPROACH NUMBER 1 -- THE BRUTE FORCE APPROACH

// IN THIS APPROACH WE WILL CALCULATE THE  MAX OF THE LEFT AND THE RIGHT MAX BUILDIND USING FOR LOOP FOR BOTH THE SIDES 


// THIS APPROACH TAKES O (N ^ 2)  COMPLEXITY
class Solution {
public:
    int trap(vector<int>& height) {
       int n = height.size();
       int ans=0;
       if(n==0) return 0;
       for(int i =1; i<= n-2 ; i++)
       {
            int l_max=0;
            for(int j = i; j>=0;j--)
            {
                l_max= max(l_max , height[j]);
            }
            int r_max=0;
            for(int j = i   ; j <n ; j++)
            {   
                r_max=max(r_max , height[j]);
            }
            if(l_max>height[i] && r_max>height[i])
            {
                ans+=min(l_max , r_max)-height[i];
            }
       }
       return ans ;  
    }
};



//APPROACH NUMBER 2 - IN THIS APPROACH WE WILL PRE COMPUTE THE LEFT MAX AND THE RIGHT MAX , DECREASING THE COMPLEXITY 
// FROM O (N ^2 )  TO  O (2n)  WHICH IS A BETTER APPROACH 

class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if (n == 0)
            return 0;
        int ans = 0;
        vector<int> l_max(n), r_max(n);
        l_max[0] = height[0];
        for (int i = 1; i < n; i++) {
            l_max[i] = max(l_max[i - 1], height[i]);
        }
        r_max[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            r_max[i] = max(r_max[i + 1], height[i]);
        }
        for (int i = 1; i < n - 1; i++) {
            ans += min(l_max[i], r_max[i]) - height[i];
        }
        return ans;
    }
};




//APPROACH NUMBER 3 - THIS IS THE OPTIMAL APPROACH 
// IN THIS APPROACH WE WILL USE THE TWO POINTER APPROACH TO SOLVE THIS PROBLEM 

class Solution {
public:
    int trap(vector<int>& height) {
        int total=0;
        int n= height.size();
        int left=0;
        int right=n-1;
        int rmax=0;
        int lmax=0;
        if(n==0) return 0 ;
        while(left<right)
        {
            lmax=max(lmax , height[left]);
            rmax=max(rmax , height[right]);


            if(lmax<rmax)
            {
                total+=lmax-height[left];
                left++;
            }
            else {
                total+=rmax-height[right];
                right--;
            }
        }
        return total ; 
    }
};



//THE MOST OPTIMAL APPROACH TO SOLVE THIS PROBLEM IS TO USE THE MONOTONIC STACK - WHICH WILL GIVE RESULT IN THE  O(N) COMPLEXITY


// APPRPOACH NUMBER 4  - THE DECREASING MONOTONIC STACK


class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int ans = 0;
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && height[i] > height[st.top()]) {
                int current = st.top();
                st.pop();
                if (st.empty())
                    break;
                int left = st.top();
                int width = i - left - 1;
                int boundedHeight = min(height[left], height[i]) - height[current];
                ans += width * boundedHeight;
            }
            st.push(i);
        }
        return ans;
    }
};