# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterative Version
    # Time: O(n)
    # Space: O(n)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 1
        stack = [(root, 1)]
        
        while stack:
            top, depth = stack.pop()
            while top:
                if top.left or top.right:
                    depth += 1
                if top.right:
                    stack.append((top.right, depth))
                max_depth = max(max_depth, depth)
                top = top.left
                
        return max_depth

            
            



        