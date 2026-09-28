class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        print(len_s1)
        dic_s1={}

        for i in range(len(s1)): 
            if s1[i] not in dic_s1: 
                dic_s1[s1[i]] = 1 
            else: 
                dic_s1[s1[i]] = dic_s1[s1[i]] + 1

        print("dic_s1: ", dic_s1)   


        dic_s2 = {}
        for i in range(len(s2)): 
            if s2[i] not in dic_s2: 
                    dic_s2[s2[i]] = 1 
            else: 
            
                    dic_s2[s2[i]] = dic_s2[s2[i]] + 1

            if i >= len_s1:
                last_char = s2[i - len_s1] 

                dic_s2[last_char]= dic_s2[last_char]-1

                if  dic_s2[last_char] == 0 : 
                    del dic_s2[last_char] 
            if i>= len_s1-1:        

                if dic_s1 == dic_s2: 
                    return True     




              
          
               

       # print(dic_s2)            



            

        return False   


        