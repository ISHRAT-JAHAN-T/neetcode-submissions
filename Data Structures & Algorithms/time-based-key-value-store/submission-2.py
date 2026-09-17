class TimeMap:

    def __init__(self):  
        self.dic = {}
       
        

    def set(self, key: str, value: str, timestamp: int) -> None: 
        

        if key not in self.dic: 
            self.dic[key] = [(value,timestamp)] 
        else: 
            self.dic[key].append((value,timestamp))


        
        

    def get(self, key: str, timestamp: int) -> str: 
        if key not in self.dic: 
            return ""
        value = self.dic[key] 
        #print(value)  


        left = 0 
        right = len(value) - 1 

        result = ""

        while left<=right: 
            mid = (left+right) // 2

            if value[mid][1] == timestamp: 
                return value[mid][0]
            elif value[mid][1] < timestamp: 
                result = value[mid][0] 

                left = mid + 1
            else: 
                right = mid - 1    



        return result

        
