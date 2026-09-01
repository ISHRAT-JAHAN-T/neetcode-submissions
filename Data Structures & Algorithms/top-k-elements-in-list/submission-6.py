
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = { }
        for i in nums: 
            if i not in dic: 
                dic[i] = 0
            dic[i] = dic[i] + 1
        heap =[] 
        for key, value in dic.items():
            heapq.heappush(heap,(value,key))
        while len(heap)>k: 
            heapq.heappop(heap)
        result = [] 
        for key,value in heap: 
            result.append(value)
        return result                    
        