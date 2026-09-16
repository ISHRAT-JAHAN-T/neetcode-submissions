class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: 

        pairs = list ( enumerate(numbers) )
       # print(pairs) 


        
                #print(index, nbr) 
             

        left = 0 
        right = len(pairs) - 1
        result=[]

        while (left<right): 

           
                
                if pairs[left][1] + pairs[right][1]== target: 
                    #print(left,right)
                    result.append(left+1)
                    result.append(right+1)
                    return result
                elif pairs[left][1] + pairs[right][1] > target: 
                    right = right -1 
                else: 
                    left = left + 1 

        return [1,2]            


            
            



        

       