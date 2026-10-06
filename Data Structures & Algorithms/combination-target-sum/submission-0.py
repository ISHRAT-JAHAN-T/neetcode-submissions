class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = [] 
        current =[] 
        index=0 
        remaining = target

        def backtrack(index,current, remaining):  

            if remaining == 0: 
                result.append(current.copy())
                return  
            if remaining < 0 : 
                return  
            if index >= len(nums):
                return

            current.append(nums[index])

            backtrack(index,current,remaining-nums[index])

            current.pop()

            backtrack(index+1,current,remaining)    

        
        backtrack(index,current,remaining)

        return result
