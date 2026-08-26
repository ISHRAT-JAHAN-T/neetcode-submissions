class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        dic = { }
        
        dic = { } 
        seen = set()
        result = []
        

        for char in range(len(strs)): 
            #print(strs[char]) 
            count = [0]*26 
            for i in range( len(strs[char] )): 
                
                value = ord(strs[char][i]) - ord('a')
                count[value] = count[value] + 1 
            
            
            #print(strs[char],count) 
            ans = tuple(count)
            if ans not in dic: 
                dic[ans] = [] 
            dic[ans].append(strs[char] )
            #result.append(dic[ans])

        #print(dic) 
        for key, value in dic.items(): 
            #print("key value", key, value)
            result.append(value)
        #result.append(dic.value)  
        #print(result)    
            


            

        return result 