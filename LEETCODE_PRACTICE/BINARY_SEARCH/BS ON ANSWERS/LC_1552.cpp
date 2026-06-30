// LEETCODE PROBLEM NUMBER 1552 - MAGNETIC FORCE BETWEEN BALLS 
// THIS PROBLEM IS SOLVED USING THE BS ON ANSWERS + GREEDY ALGORITHM 
class Solution {
public:
    bool Placed(vector<int>&position , int distance , int balls)
    {
        int ball_count=1;
        int last_pos=position[0];
        for(int i =1 ; i< position.size();i++)
        {
            if(position[i]-last_pos>=distance)
            {
                ball_count++;
                last_pos=position[i];
            }
            if(ball_count>=balls)
            {
                return true ;
            }
        }
        return false;
    }
    int maxDistance(vector<int>& position, int m) {
        sort(position.begin(), position.end());
        int low=1;
        int high=position[position.size()-1] - position[0];
        while(low<=high)
        {
            int mid = low + (high-low)/2;
            if(Placed(position,mid , m)==true)
            {
                low=mid+1;
            }
            else {
                high=mid-1;
            }
        }
        return high ;
    }
};