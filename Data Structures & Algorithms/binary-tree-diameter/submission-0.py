# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: 

        ans = [0]
        def depth(root):
            if root is None: 
                return 0 

            left =depth(root.left)
            right= depth(root.right)

            diameter = left + right 
            ans[0] = max(ans[0],diameter)

            return max (left,right) + 1

        depth(root)    

        return ans[0]   

        






        