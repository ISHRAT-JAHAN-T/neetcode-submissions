class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = [] 
        current =[] 
        index=0 
        remaining = target

        candidates.sort()    


        def backtrack(index,current, remaining):  

            if remaining == 0: 
                result.append(current.copy())
                return  
            if remaining < 0 : 
                return  
            if index >= len(candidates):
                return 



            current.append(candidates[index])

            backtrack(index+1,current,remaining-candidates[index])

            current.pop() 

            next_index = index + 1

            while (
                next_index < len(candidates)
                and candidates[next_index] == candidates[index]
            ):
                next_index+= 1



  
            backtrack(next_index,current,remaining)    

        
        backtrack(index,current,remaining)

        

        return result

        