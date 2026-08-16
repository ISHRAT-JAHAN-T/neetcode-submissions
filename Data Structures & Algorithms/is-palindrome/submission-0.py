class Solution:
    def isPalindrome(self, s: str) -> bool: 
        newstring=""
        for i in s: 
            if i.isalnum(): 
                newstring= newstring + i.lower()
       # print(newstring)   

        length= len(newstring)
       # print(length) 

        i=0 
        j=length-1 

        for i in range(length//2):
           # print(newstring[i], " ", newstring[j]) 
            if newstring[i]!=newstring[j]: 
                return False
            j=j-1

        return True       
            
        