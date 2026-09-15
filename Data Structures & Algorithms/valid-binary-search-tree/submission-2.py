# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS Recursion Solution
    # Time: O(n)
    # Space: O(h) due to recursion stack, at worst O(n) for skewed tree
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, lower=None, upper=None):
            if node is None:
                return True

            if lower is not None and node.val <= lower:
                return False

            if upper is not None and node.val >= upper:
                return False

            return (
                valid(node.left, lower, node.val)
                and valid(node.right, node.val, upper)
            )

        return valid(root)