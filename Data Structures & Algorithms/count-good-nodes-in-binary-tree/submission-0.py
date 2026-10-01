# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        current_max = root 
        node = root
        count=0
        
        def dfs(node,current_max):
            nonlocal count 
            if node is None: 
                return
            if node.val > current_max.val: 
                current_max = node 
            if current_max.val==node.val: 
                count = count +1 

            dfs(node.left,current_max)
            dfs(node.right, current_max)  

        dfs(node, current_max)    

        return count

        