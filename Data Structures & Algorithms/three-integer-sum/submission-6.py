class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        nums.sort() 
        #print(nums) 
        result = []
        

        for i in range(len(nums)-1): 
            #print(i) 
           # print(nums[i])
           
            if i > 0 and nums[i] == nums[i-1] : 
                #print(" i am here", nums[i], nums[i-1],i)
               
                continue
        
            

            left = i + 1
            right = len(nums) - 1
            target = nums[i] 
           # print(target)


            while left < right :
                    
                   # print ( target , nums[left], nums[right])
                    answer = target + nums[left] + nums[right]
                
                    if answer == 0: 
                        #print("anser",target,nums[left],nums[right])  
                        triplate = [target, nums[left], nums[right]]
                        result.append(triplate)
                        left = left + 1
                        right = right - 1
                    # skip duplicate left values
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                    # skip duplicate right values
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif answer > 0: 
                        #left = left + 1
                        right = right -1 
                    else: 
                        #right = right -1    
                        left = left + 1     


        return result