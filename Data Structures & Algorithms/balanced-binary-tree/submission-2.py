# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterative solution
    # Time: O(n)
    # Space: O(n)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, False)]
        heights = {}

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                l_height = heights.get(node.left, 0)
                r_height = heights.get(node.right, 0)

                is_balanced = abs(r_height - l_height) <= 1

                if not is_balanced:
                    return False

                heights[node] = 1 + max(l_height, r_height)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return True