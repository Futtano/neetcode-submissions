# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursive Solution
    # Time: O(m*n) where m in the number of nodes in root and n is the number of nodes in subRoot
    # Space: O(h) where h is the height of root (at worst, for a skewed tree can be O(m+n))
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def checkTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            
            return (
                root.val == subRoot.val and
                checkTree(root.left, subRoot.left) and
                checkTree(root.right, subRoot.right)
            )

        if checkTree(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )
        