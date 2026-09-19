# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([root])

        count = 0

        while queue:
            level_size = len(queue)

            for i in range(level_size): 

                node = queue.popleft()
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)



               # print(node.val)


                    
            count = count + 1    
        return count        