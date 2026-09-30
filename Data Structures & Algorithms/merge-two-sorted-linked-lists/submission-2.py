# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        
        
        dami = ListNode() 
        answer = dami
        while list1 and list2:  
            if list1.val < list2.val: 
                dami.next = list1 
                list1 = list1.next  
                
            else: 
                dami.next = list2 
                list2 = list2.next 
            dami= dami.next    
        if list1: 
            dami.next = list1 
            
        else:
            dami.next = list2  
            

        return answer.next                 

        