class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        n = len(nums) 
        right = n-1 
        left = 0
        #mid = n//2 
        #print("mid",nums[mid])   
        if len(nums)==1 and nums[0] == target: 
            return 0
        
        
        while(left<right): 
            mid = int((left+right) / 2) 
            
            print("left right mid", left, right, mid)
            if nums[mid] == target: 
                return mid
            elif target>nums[mid]: 
                left = mid+1 
            else: 
                right = mid  
        if left==right: 
            if nums[left]==target: 
                return left        

    
        return -1
        