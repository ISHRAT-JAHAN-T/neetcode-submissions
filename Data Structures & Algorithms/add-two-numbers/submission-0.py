# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        #reverse the linked list 
        prev_node = None 
        current_node = l1 
       

        while(current_node): 
            next_node = current_node.next 
            current_node.next = prev_node
            prev_node = current_node 
            current_node = next_node 
           
        number_1 = prev_node.val
        print(number_1)
        while(prev_node.next): 
           # print(prev_node.next.val)
            number_1 = number_1 * 10 + prev_node.next.val
            prev_node = prev_node.next  
            print(number_1)
       # number_1 = numer_1 * 10 + prev_node.val  
        #number_1 = ((number_1 * 10) + prev_node.val )
        print("numberone",number_1)   


        #reverse for the linked list two l2 
        prev_node = None 
        current_node = l2
       

        while(current_node): 
            next_node = current_node.next 
            current_node.next = prev_node
            prev_node = current_node 
            current_node = next_node 
           
        number_2 = prev_node.val
        print("2",number_2)
        while(prev_node.next): 
           # print(prev_node.next.val)
            number_2 = number_2 * 10 + prev_node.next.val
            prev_node = prev_node.next  
       # number_1 = numer_1 * 10 + prev_node.val  
        #number_2 = ((number_2 * 10) + prev_node.val )
        print(number_2)  

        result = number_1 + number_2 
       # print("result",result)  


        divider = result // 10
        division = result % 10
        result = divider
        print(division) 
        old_node = ListNode(division)
        updated = old_node
        test = updated

        while(result!=0): 
            divider = result // 10
            division = result % 10
            result = divider
           # print(division) 
            new_node = ListNode(division) 
            old_node.next =new_node 
            old_node = new_node 

        while(test): 
           # print(test.val)
            test = test.next    

        




        return updated   



        