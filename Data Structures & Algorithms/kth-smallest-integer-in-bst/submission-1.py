# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS Recursion
    # Time: O(h + k) depth traversal and then k moves to find the answer
    # Space: O(h) for the recursion stack
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def dfs(node):
            nonlocal count

            if node is None:
                return None

            # Search smaller values first
            result = dfs(node.left)
            if result is not None:
                return result

            # Visit current node
            count += 1
            if count == k:
                return node.val

            # Search larger values
            return dfs(node.right)

        return dfs(root)