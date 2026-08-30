# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        stack = [] 
        result = head 
        while(head): 
            stack.append(head)
            head= head.next  

        if n == len(stack): 
            return result.next    
        target_index = len(stack) - n 

        prev = stack[target_index-1]
        target = stack[target_index] 
        prev.next = target.next 
        return result
        
               


        