# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
"""
# Approach: BFS (Level Order Traversal)
# 1. Use a queue to store (node, level).
# 2. Start with the root at level 0.
# 3. Pop each node and store its value according to its level.
# 4. Add left and right children to the queue with level + 1.
# 5. Convert the level dictionary into a 2D list.
#
# Time: O(n)
# Space: O(n) 
"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 

        if root is None:
            return [] 

        queue = [] 
        pair = (root,0)
        queue.append(pair)
        count=0 

        dic={ }
         

        while queue: 
            
            node, level = queue.pop(0)
            #print(node.val, level)
            #print(node.val)  
            if level not in dic: 
                dic[level] =[] 
            dic[level].append(node.val)    

            
            if node.left : 
                
                pair = (node.left , level+1)
                queue.append(pair)
            if node.right: 
                
                pair = (node.right, level+1)
                queue.append(pair) 

            #print("queue",queue)  
            #print(dic)  
        result = []    
        for index, value in dic.items(): 
           # print(index,value) 
            
            result.append(value)
        #print(result)    





        

        return result



        