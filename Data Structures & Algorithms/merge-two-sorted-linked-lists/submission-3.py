# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
1. Compare the current nodes of list1 and list2.
2. Add the smaller node to the merged list.
3. Move forward in the list from which the node was taken.
4. When one list ends, attach the remaining part of the other list.

5.Time Complexity: O(n + m)
6.Space Complexity: O(1)
"""


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

        