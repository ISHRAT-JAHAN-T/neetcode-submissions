# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        result = False
        if root is None: 
            return False 
        if subRoot is None: 
            return True    
        if root.val == subRoot.val: 
            result= self.match(root,subRoot) 

        if result == True: 
            return True
       
        left= self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right            


    def match(self,root, subRoot): 
        if root is None and subRoot is None: 
            return True 
        elif root is None and subRoot is not None: 
            return False  
        elif root is not None and subRoot is None: 
            return False 
        elif root.val != subRoot.val: 
            return False 
        
        left = self.match(root.left, subRoot.left)
        right= self.match(root.right, subRoot.right)

        if left == True and right == True: 
            return True 
        else: 
            return False       
                    

        