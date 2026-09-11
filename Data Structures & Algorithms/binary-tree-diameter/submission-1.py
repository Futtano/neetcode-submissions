# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(n)
    # Space: O(h) where h is the height of the tree
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(node):
            nonlocal diameter

            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            diameter = max(
                diameter,
                left_height + right_height
            )

            return 1 + max(left_height, right_height)

        height(root)
        return diameter