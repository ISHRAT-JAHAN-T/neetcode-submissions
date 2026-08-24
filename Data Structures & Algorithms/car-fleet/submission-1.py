class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 
        cars = list(zip(position, speed))

        #print(cars)
        cars.sort(key=lambda x: x[0], reverse=True)

        #print(cars)   
        stack = [] 

        for position, speed in cars: 
            time = (target - position)/speed 
            #print("position speed time target", position, speed, time, target) 
            stack. append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2] : 
                stack.pop()
        return len(stack)        

        

        
        
        
        
        return 1

        