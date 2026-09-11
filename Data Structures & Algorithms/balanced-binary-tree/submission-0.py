# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0, True

            l_height, l_balanced = check(root.left)
            r_height, r_balanced = check(root.right)

            diff = abs(l_height - r_height)

            this_balanced = l_balanced and r_balanced and diff <=1

            return (1 + max(l_height, r_height), this_balanced)
        
        return check(root)[1]