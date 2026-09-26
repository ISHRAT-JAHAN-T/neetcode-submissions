class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic= { } 
        
        left = 0 
        max_result = 0
    
        for right in range(len(s)):
            if s[right] not in dic : 
                dic[s[right]] = 1
            else: 
                 dic[s[right]] =  dic[s[right]] + 1

           # print(dic)    
            current_window_length = (right - left) + 1
           # print(current_window_length) 
            max_frequency = max(dic.values()) 
           # print(max_frequency)
            replacement = current_window_length - max_frequency 

            if replacement <= k: 
               # print("valid")
                if current_window_length > max_result: 
                    max_result = current_window_length
            else: 
             #   print("invalid") 
                dic[s[left]] = dic[s[left]] - 1
                left = left + 1    





            



        return max_result       



        