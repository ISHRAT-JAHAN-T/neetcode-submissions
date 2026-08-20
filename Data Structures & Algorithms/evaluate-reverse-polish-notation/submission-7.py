class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        for i in tokens: 
            if i not in ['+','-','*','/']:
                stack.append(int(i))
            else:  
                b=stack.pop()
                a=stack.pop() 
                #print(" b a", b, a) 
                ##a= int(a)
                if i =="+": 
                    result = a + b 
                    stack.append((result))
                elif i == "-":
                    result = a - b 
                    stack.append((result))  
                elif i == '*': 
                    result = a * b 
                    stack.append((result))  
                elif i == '/': 
                    result = a / b 
                    stack.append(int(result))            
        return stack[-1]   
        