# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:  

        
        res_one = [] 
        res_two = []

        def same_tree_one(root): 
            if root is None: 
                res_one.append("None")
                return 0
            print(root.val)
            res_one.append(root.val)

            same_tree_one(root.left)
            same_tree_one(root.right) 
        def same_tree_two(root): 
            if root is None: 
                res_two.append("None")
                return 0
            print(root.val)
            res_two.append(root.val)

            same_tree_two(root.left)
            same_tree_two(root.right)
    
    



        same_tree_one(p)  
        same_tree_two(q)   
        if res_one==res_two: 
            return True
        else: 
            return False    
        

        