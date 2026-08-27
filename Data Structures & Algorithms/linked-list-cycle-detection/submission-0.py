# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = { }
        while(head): 
            if head.next not in dic: 
                dic[head.next] =[]

                dic[head.next].append(head.next)
                head = head.next 
            else: 
                return True 
        return False            
                
        