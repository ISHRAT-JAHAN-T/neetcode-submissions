class Solution:
    def maxProfit(self, prices: List[int]) -> int: 

        left = 0
        right = 1

        #print("left right", left)   
        max_value = 0

        while(right< (len(prices))): 
             
            print("left right ", prices[left],prices[right]) 

            if prices[left] > prices[right] : 
                left = right 
                right = right + 1 
            else:  
                ans = prices[right] - prices[left] 
                if ans>max_value: 
                    max_value = ans 
                right = right+1   
            print("max_value", max_value)     


        return max_value

        