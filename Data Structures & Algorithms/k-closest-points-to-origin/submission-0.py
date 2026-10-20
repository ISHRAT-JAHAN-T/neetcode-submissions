import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mine_heap =[]


        for x,y in points: 
            distance = x*x + y*y 
            heapq.heappush(mine_heap, (distance,x,y))


        result = [] 
        for i in range(k): 
            distance, p, q = heapq.heappop(mine_heap) 
            result.append([p, q]) 
        return result    



        