class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:  
        
        dic= {}
        for i in nums: 
            #print(nums)  
            if i not in dic:  
                dic[i]= [] 
                
            dic[i].append(i)  

        print(dic)  

        for i in dic:  
           # print(i, "   ",  len(dic[i]))
            if len(dic[i]) >= 2: 
                return True
        return False     

        