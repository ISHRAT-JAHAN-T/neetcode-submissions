class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        dic={}
        for i in strs: 
            
            sorted_string = "".join(sorted(i))  
        
            if sorted_string not in dic:

                dic[sorted_string]=[]  
           
            if sorted_string in dic:   
               
                dic[sorted_string].append(i)

            
        return list(dic.values())

        