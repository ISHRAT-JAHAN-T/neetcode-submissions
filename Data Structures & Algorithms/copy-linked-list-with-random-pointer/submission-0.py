"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {None: None}
        current = head
        while(current): 
            new_node = Node(current.val)
            dic[current]=new_node
            current = current.next

        current = head 
        while(current):      
            dic[current].next = dic[current.next]    
            dic[current].random = dic[current.random]
            current = current.next 
        return dic[head]    
            

