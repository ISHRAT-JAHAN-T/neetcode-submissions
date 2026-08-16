class Solution:

    def encode(self, strs: List[str]) -> str:  
        result="" 
        encode_string= "tonny"
         #print(strs)  
        for i in strs: 
             #print(i)
            result= result+i + encode_string
         #print("here is the encoded result: ")
         #print(result)    
        return result

    def decode(self, s: str) -> List[str]: 
        result=[]
        #print(s)  
        
        result = s.split("tonny")   
        print(result) 

        if result and result[-1]=="": 
            result.pop() 
        print("my output:")    
        print(result)    

        return result
