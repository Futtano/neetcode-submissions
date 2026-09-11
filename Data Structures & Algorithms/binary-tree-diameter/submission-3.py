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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        stack = [(root, False)]
        heights = {}

        while stack:
            node, is_visited = stack.pop()

            if not node:
                continue

            if is_visited:
                l_height = heights.get(node.left, 0)
                r_height = heights.get(node.right, 0)

                diameter = max(diameter, l_height + r_height)

                heights[node] = 1 + max(l_height, r_height)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        
        return diameter