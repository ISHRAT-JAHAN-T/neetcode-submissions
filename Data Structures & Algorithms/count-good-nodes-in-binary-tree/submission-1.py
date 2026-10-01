"""
1. Approach: DFS
2. Keep track of the maximum value seen on the path from the root to the current node.
3. If the current node >= current_max, it is a good node.
4. Pass the updated current_max to both the left and right subtrees.
5. Time Complexity: O(n)
6. Space Complexity: O(h) for the recursion stack.
"""









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

        