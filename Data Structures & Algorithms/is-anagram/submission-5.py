class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        s= sorted(s) 
        t=sorted(t)  
        
        
        
       
          

        dic_s={ }
        dic_t={ }  
        count=0

        

        for i in s:  
            if i not in dic_s: 
                dic_s[i]=0
            dic_s[i]=  dic_s[i] +1

       


        for i in t:  
            if i not in dic_t: 
                dic_t[i]=0 
            dic_t[i] = dic_t[i] +1

        
        
        if dic_s == dic_t:
            return True 
        
        return False        
   



        
