class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        self.min=999999
        

    def push(self, val: int) -> None:
        
        self.stack.append(val) 
        if val < self.min: 
            self.min=val 
            self.min_stack.append(val) 

        

    def pop(self) -> None:   
        if self.stack: 
            self.stack.pop() 
        if self.min_stack:    
            self.min_stack.pop()

        

    def top(self) -> int: 
        top_item = self.stack[-1]
        return top_item
        

    def getMin(self) -> int: 
        min_number = min(self.stack)
        return min_number
        
