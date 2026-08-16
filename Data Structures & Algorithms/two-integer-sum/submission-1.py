class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        dic={ }
        j=0
        for i in nums: 
            sub = target - i 

            if sub not in dic: 
            
                dic[i]=j
            else:  
                #print("hellow world")  
                a=dic[sub]  
                b=j
               # print(a,b)
                return [a,b]
              

            j=j+1 

                   
        print(dic)

        return []              

        