# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next 


# Linked List Cycle - Review Notes
#
# Strategy:
# - Traverse the linked list.
# - Store each visited NODE in a set.
# - If the same node appears again -> cycle exists.
# - If we reach None -> no cycle.
#
# Pattern:
# "Have I seen this before?" -> think SET
#
# Time: O(n)
# Space: O(n)
#
# What I learned:
# - head is a reference to a ListNode object.
# - head.val = value inside the node.
# - head.next = reference to the next node.
# - For cycle detection, compare NODE objects, not node values.
# - Set is better than dictionary when I only need seen/not-seen.
#
# My initial mistakes:
# - Used a dictionary even though I didn't need key:value pairs.
# - Used dic[node].append(node), but the dictionary value didn't exist yet.
# - Initially focused on head.next instead of simply tracking head.
#
# Remember:
# Dictionary -> need key:value
# Set        -> only need "have I seen it?"
#
# Improvement:
# Learn Floyd's slow/fast pointer solution -> O(n) time, O(1) space.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen  = set()
        while(head): 
            if head.next not in seen: 
                seen.add(head.next)
                head = head.next
            else: 
                return True 
        return False            
                
        