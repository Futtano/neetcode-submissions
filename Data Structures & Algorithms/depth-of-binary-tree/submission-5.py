# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterative BFS: count tree levels
    # Let n be the number of nodes and w the maximum width of any level.
    # Time complexity: O(n)
    # Space complexity: O(w): O(1) for a chain, O(n) worst case
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([root])
        maxDepth = 0

        while queue:
            n = len(queue)
            maxDepth += 1
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return maxDepth