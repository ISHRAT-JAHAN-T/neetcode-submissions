class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        dic = { }
        result = []
        for i in range(len(nums)): 
            sub_value = target - nums[i]
            if sub_value not in dic: 
                dic[nums[i]] = i  
            else: 
                
                result.append(dic[sub_value]) 
                result.append(i)   
            

            
        #print("result",result)   
        return result  

        