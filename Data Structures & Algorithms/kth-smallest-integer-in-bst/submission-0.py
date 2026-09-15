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
        n = 0
        res = None

        def dfs(root):
            nonlocal n, res

            if root is None or res is not None:
                return

            dfs(root.left)

            # Left subtree may have found the answer
            if res is not None:
                return

            n += 1
            if n == k:
                res = root.val
                return

            dfs(root.right)

        dfs(root)
        return res