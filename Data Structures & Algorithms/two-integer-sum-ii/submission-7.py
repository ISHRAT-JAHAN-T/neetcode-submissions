class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        result = []

        for i in range(len(numbers)):

            
          
            
            sub = target - numbers[i] 


            
            if sub not in dic:
                dic[numbers[i]] = i

            else:
                index = dic[sub]
                print(index, i)

                result.append(index + 1)
                result.append(i + 1)
                break

        return result