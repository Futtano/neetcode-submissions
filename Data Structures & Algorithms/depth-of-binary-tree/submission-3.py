# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursive Version
    # Time: O(n)
    # Space: O(n) (best case O(h) where h is the height of the tree only if the tree is balanced)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        return Solution.dive(root, depth)

    @staticmethod 
    def dive(node: Optional[TreeNode], lastdepth:int) -> int:
        if not node:
            return lastdepth
        
        lastdepth += 1
        return max(Solution.dive(node.left, lastdepth), Solution.dive(node.right, lastdepth))