# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative preorder DFS: node → left subtree → right subtree
    # Let n be the number of nodes and h the tree's height.
    # Time complexity: O(n)
    # Space complexity: O(h) auxiliary stack; O(n) output
    #                   O(n) total including output
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            # Append current node before processing children
            res.append(node.val)
            # Stack is LIFO, since we need to append
            # node -> left -> right we need to insert
            # right first and then left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res
