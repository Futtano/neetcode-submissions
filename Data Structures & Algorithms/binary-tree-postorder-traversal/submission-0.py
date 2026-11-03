# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative postorder DFS with deferred parent visits
    # Let n be the number of nodes and h the tree's height.
    # Time complexity: O(n)
    # Space complexity: O(h) auxiliary stack; O(n) output
    #                   O(n) total including output
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        # (node, isReady), isReady=True means that both left and right
        # subtrees have been processed when we pop this node again,
        # so the node can be appended at the next pop
        stack = [(root, False)]

        res = []

        while stack:
            node, isReady = stack.pop()
            if isReady:
                res.append(node.val)
            else:
                # Append the current node first
                # with isReady=True and then
                # right and left children in this order so that
                # when we pop this node again we're sure we've
                # processed both left and right subtrees
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return res