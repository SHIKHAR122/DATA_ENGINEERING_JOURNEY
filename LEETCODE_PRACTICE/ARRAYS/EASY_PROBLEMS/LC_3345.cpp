// LEETCODE PROBLEM NUMBER 3345 - SMALLEST DIVISIBLE DIGIT PRODUCT -I 


// IN THIS PROBLEM WE WILL FIND THE RANGE TILL WHICH WE HAVE TO FIND THE SMALLEST DIVISIBLE  - BY SIMPLY ADDING 10+N TO THE DIGIT
// THEN TRAVERSE FROM N TO FINAL_RANGE AND CHECK IF THE PRODUCT OF THE DIGITS ARE DIVISIBLE BY t OR NOT IF THEY ARE THEN STORE THEM
//  AS THE MINIMUM OR ELSE SIMPLY CONTINUE TO SEARCH IN THE RANGE 


class Solution {
public:
    int productOfNum(int num)
    {
        int product=1;
       while (num > 0) {
        int digit = num % 10; // Get the last digit
        product *= digit;        // Multiply it to the total
        num/= 10;    // Remove the last digit
              
    }
        return product;    
    }
    int smallestNumber(int n, int t) { //n is the number 
        int final_range= n+10;
        int minimum_answer=INT_MAX;
        
        for(int i=n;i<=final_range;i++)
        {   
            int product=productOfNum(i);
            if(product%t==0)
            {
                minimum_answer=min(minimum_answer , i);
            }
            else {
                continue;
            }
        }
        return minimum_answer;
    }   
};