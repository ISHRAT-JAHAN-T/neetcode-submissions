class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        dic_1 = { }
        dic_2 = { }

        for i in s: 
            if i not in dic_1: 
                dic_1[i] =[]
                 
            dic_1[i].append(i)  
        for key , value in dic_1.items(): 
            print("key and value", key, len(value))       
                
        #print(dic_1) 

        for i in t: 
            if i not in dic_2: 
                dic_2[i] =[]
                 
            dic_2[i].append(i)  
        #for key , value in dic_2.items(): 
            #print("key and value", key, len(value))       
                
       # print(dic_2)   

        if dic_1 == dic_2: 
           # print("True") 
            return True
        else: 
           # print("False")  
            return False  

      


        
        