# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(log2(n)) where n is the number of nodes, worst case O(n) is the tree is highly unbalanced
    # Space: O(1)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while True:
            if cur.val > max(p.val, q.val):
                cur = cur.left
            elif cur.val < min(p.val, q.val):
                cur = cur.right
            else:
                return cur