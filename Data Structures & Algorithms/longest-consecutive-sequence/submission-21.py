class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        seen = set()
        seen = set(nums) 



        print(seen)
        max_length = 0

        

        

        for i in range(len(nums)): 
            starting = nums[i] - 1
            
            if starting not in seen:
                current = nums[i]
                length = 1 

                while current + 1 in seen: 
                    current = current + 1 
                    length = length + 1
                

        
                if length > max_length: 
                    max_length = length     
           




        return max_length
        