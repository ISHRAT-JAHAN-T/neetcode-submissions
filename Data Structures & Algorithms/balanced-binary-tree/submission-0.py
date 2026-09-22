# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool: 
        #ans = [0]
        balanced = [True]
        def depth(root):
            if not root: 
                return 0 

            left =depth(root.left)
            right= depth(root.right)

            #diameter = left + right 
            #ans[0] = max(ans[0],diameter) 

            if abs(left - right) > 1:
                balanced[0] = False 
                return 0 
          

            return 1+max(left,right) 

        depth(root)   
        return balanced[0] 

        
        