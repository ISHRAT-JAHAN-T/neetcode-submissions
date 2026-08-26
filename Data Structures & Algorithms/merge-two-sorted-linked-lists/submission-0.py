# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        demo = ListNode()
        new_list = demo 

        while ( list1 and list2 ): 
            if ( list1.val < list2.val ): 
                new_list.next = list1 
                list1 = list1.next 
                new_list = new_list.next 
            else: 
                new_list.next = list2 
                list2 = list2.next 
                new_list = new_list.next    
        while(list1): 
            #print("still list1 is left", list1.val)
            new_list.next = list1 
            list1 = list1.next 
            new_list = new_list.next 
        while(list2): 
            #print("still listw is left", list2.val) 
            new_list.next = list2 
            list2 = list2.next 
            new_list = new_list.next 


           
        

        return demo.next
      
      
        
        
                
                

        


                





        