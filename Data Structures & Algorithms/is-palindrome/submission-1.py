class Solution:
    def isPalindrome(self, s: str) -> bool: 
        
        result =[]
        for char in s:
            #print(char) 

            if char.isalnum(): 
                result.append(char.lower()) 
       # print(result)     
       

        left = 0 
        right = len(result) - 1
       # print("left right",left, right ) 

        while(left<right): 
            if result[left] != result[right]: 

                return False
            left = left +1 
            right = right -1     
            

        return True   
        