# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        current = head  


        while current: 
            next = current.next 
            current.next = prev 
            prev = current
            current = next 
        """    
        while prev: 
            print(prev.val)
            prev = prev.next   
        """ 
        return prev    
        