import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:    

        heap = []
        for x in stones: 
            heap.append(-x) 
        heapq.heapify(heap)

        #print("max heap", heap)   

        while len(heap) >1 : 
            x = - (heapq.heappop(heap))
            y = - (heapq.heappop(heap)) 

            if x != y: 
                difference = x - y
                heapq.heappush(heap, - difference)
            if len(heap)==0: 
                return 0 
        return -heap[0]              


        