# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Optimal DFS solution
    # Time: O(n)
    # Space O(h) where h is the height of the three (at worst O(n))
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(node):
            nonlocal res

            if node is None:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Best complete path whose highest node is `node`
            res = max(res, node.val + left + right)

            # Parent can only continue through one branch
            return node.val + max(left, right)

        dfs(root)
        return res