class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = { } 

        for i in nums: 
            if i not in dic: 
                dic[i] = [] 
            dic[i].append(i)
        #print(dic) 

        for key,value in dic.items():
            
            #print("key and value",key,len(value))
            if len(value) >= 2: 
                return True

        return False       