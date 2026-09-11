# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(n)
    # Space: O(h) where h is the height of the tree
    def __init__(self):
        self.max_diam = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.calculateDiam(root)
        return self.max_diam

    def calculateDiam(self, node):
        if not node:
            return -1

        depth_left = 1 + self.calculateDiam(node.left)
        depth_right = 1 + self.calculateDiam(node.right)

        diam = depth_left + depth_right
        self.max_diam = max(self.max_diam, diam)

        return max(depth_left, depth_right)

        
        

        

            
        