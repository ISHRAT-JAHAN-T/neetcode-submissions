class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        #left_side_calculation 

        
        left_result=[] 
        multi = 1
        #left_result.append(0)
        for i in range(len(nums)):  
            if i == 0:
                left_result.append(1)
            else:    
                multi = multi * nums[i-1] 
                left_result.append(multi) 
        #print("left result",left_result)  

        #right_side  
        right_result = [] 
        multi = 1 
        for i in range(len(nums)-1,-1,-1): 
            if i == len(nums)-1: 
                right_result.append(1)
            else: 
                multi = multi * nums[i+1] 
                right_result.append(multi) 
        
        right_result.reverse() 
        #print("right result", right_result)
        result = [] 

        for i in range(len(right_result)): 
            result.append(right_result[i]*left_result[i])     

        return result
            




        