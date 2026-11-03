# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative inorder DFS: left subtree → node → right subtree
    # Let n be the number of nodes and h the tree's height.
    # Time complexity: O(n)
    # Space complexity: O(h) auxiliary explicit stack;
    #                   O(n) output, hence O(n) total
    # h = O(log n) if balanced; O(n) worst case.
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []
        stack = [root]
        current = root.left

        while current is not None or stack:
            if current is None:
                node = stack.pop()
                res.append(node.val)
                current = node.right
            else:
                stack.append(current)
                current = current.left 
        

        return res