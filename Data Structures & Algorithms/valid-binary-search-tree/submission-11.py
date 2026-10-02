"""
Approach: DFS with valid range

1. Every node must stay within an allowed (minimum, maximum) range.
2. Start the root with (-infinity, +infinity).
3. If we go LEFT:
   - minimum stays the same
   - current node value becomes the new maximum.
4. If we go RIGHT:
   - current node value becomes the new minimum
   - maximum stays the same.
5. If node.val <= minimum or node.val >= maximum, it is not a valid BST.
6. Both left and right subtrees must be valid.

Time Complexity: O(n)
Space Complexity: O(h) for the recursion stack.
"""






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       

        def dfs(node, minimum, maximum):

            if node is None:
                return True

            
            if node.val <= minimum or node.val >= maximum:
                return False

           
            left = dfs(node.left, minimum, node.val)

           
            right = dfs(node.right, node.val, maximum)

          
            return left and right

        return dfs(root, float("-inf"), float("inf") )