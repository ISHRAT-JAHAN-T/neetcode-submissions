# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: 
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
           tempo = value[-1]
            
           result.append(tempo)
        #print(result)  

        return result




        