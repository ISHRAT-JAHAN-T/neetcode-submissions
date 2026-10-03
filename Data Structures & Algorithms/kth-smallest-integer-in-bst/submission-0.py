# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:  

        count =0 
        result = None
        def traversal(root,k):
            nonlocal count 
            nonlocal result

            if root is None: 
                return 

            traversal(root.left,k) 
            count = count + 1 
            #print("count k", count,k)
            if count==k:
            
             print(root.val)
             result = root.val
              
              #return root.val
              

            traversal(root.right,k) 
        traversal(root,k)     

        return result 


            

        