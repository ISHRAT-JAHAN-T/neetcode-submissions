class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 

        dic = {}
        for i in (nums): 
            if i not in dic: 
                dic[i]=[] 
            dic[i].append(i)
        #print(dic)  
        for key, value in dic.items(): 
            dic[key] = len(value)
        #print(dic)  
        dic = dict(sorted(dic.items(), key= lambda x:x[1], reverse = True))  
        #dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True)) 
        result = []
        target = 1 
        for key, value in dic.items(): 
            if target<=k: 
                result.append(key) 
            target = target+1    

        return result
        