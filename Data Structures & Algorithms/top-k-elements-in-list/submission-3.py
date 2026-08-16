class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic= {}  
        import heapq
        heap=[] 

          
        

        for i in nums: 
            if i not in dic:
                dic[i]=0
                
            dic[i]=dic[i]+1
        


        for i in dic:  
            frequency = dic[i] 

            if len(heap) < k: 
                heapq.heappush(heap, (frequency,i))
           
            elif frequency > heap[0][0]:
                  heapq.heappop(heap)    
                  heapq.heappush(heap, (frequency,i))  

            result= [] 
            for frequncey, number in heap: 
                #print("this is frequncey", frequency)
                #print("this is my numebr", number)   
                result.append(number)    


        return result   

        
              


        return heap   