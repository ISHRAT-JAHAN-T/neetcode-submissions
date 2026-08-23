class Solution:
    def maxArea(self, heights: List[int]) -> int: 
        left = 0 
        right = len(heights) - 1
       # print(left, right) 
        max_number = 0 

        while left < right: 

            weight = right - left 
            height = min (heights[right], heights[left]) 
            #print(weight,height)  
            comtainer = weight * height 
            #print("container", comtainer) 

            if comtainer  > max_number : 
                max_number = comtainer  

            if heights[left] < heights[right]: 
                left = left + 1
            else: 
                right = right -1    


       # print(max_number)
        return max_number 

   
            





        
        