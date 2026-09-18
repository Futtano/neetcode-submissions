# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Overly complicated DFS solution
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return root.val

        res = float('-inf')

        def updateMaxPath(root):
            nonlocal res

            if root.left is None and root.right is None:
                res = max(res, root.val)
                return root.val

            if root.left:
                leftMax = updateMaxPath(root.left)

            if root.right:
                rightMax = updateMaxPath(root.right)

            if root.left and root.right:
                biggestPathSum = max(
                    root.val + leftMax + rightMax,
                    root.val + leftMax,
                    root.val + rightMax,
                    root.val,
                )

                pathToReturn = max(
                    root.val + leftMax,
                    root.val + rightMax,
                    root.val,
                )

            elif root.right:
                biggestPathSum = max(
                    root.val,
                    root.val + rightMax
                )

                pathToReturn = biggestPathSum

            else:
                biggestPathSum = max(
                    root.val,
                    root.val + leftMax
                )

                pathToReturn = biggestPathSum

            res = max(res, biggestPathSum)

            return pathToReturn

        updateMaxPath(root)
        return res