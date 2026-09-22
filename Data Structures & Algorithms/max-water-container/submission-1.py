class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1

        print("left right", left, right) 

        maximum_number = 0 

        while left<right: 
            ans = (right-left)* min(heights[left],heights[right])

            print("ans")
            if ans > maximum_number: 
                maximum_number = ans  


            if heights[left] < heights[right]: 
                left = left+1
            else:
                right = right - 1       

        return  maximum_number 

        