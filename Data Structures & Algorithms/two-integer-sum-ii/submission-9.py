class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: 
        result = []
        right = 0 
        left = len(numbers) - 1
        for i in range(len(numbers)): 
           # print("i, numbers[i]", i , numbers[i])
            sum_nbr = numbers[right] + numbers[left]
            if sum_nbr== target: 
                result.append(right+1) 
                result.append(left+1)
                break
            elif sum_nbr > target: 
                left = left - 1
            else: 
                right = right + 1    

        return result    
        

        