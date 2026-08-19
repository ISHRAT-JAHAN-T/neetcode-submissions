class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        #print(nums) 
        if len(nums) == 1: 
            return 1 


        if len(nums) == 0:
            return 0    
        ans= sorted(nums) 
        
        #print("hellow world")
        #print(ans)
        seen=set() 

        max_length=1
        count=0

        for i in range(len(ans)-1): 
           # print(ans[i]) 
          
            if (ans[i+1] - ans[i] ==1 or ans[i+1] - ans[i] ==0) and (ans[i+1] not in seen or  ans[i] not in seen) :

             
               
                seen.add(ans[i])  
                seen.add(ans[i+1]) 
               
            elif ans[i+1] - ans[i] >1: 
                
                seen=set() 
                count=1
              
            current_length= len(seen) 
            if max_length<current_length: 
                max_length=current_length  
                
        #print("answer",seen)  
        result= len(seen)     
        
        
           

        return max_length
        