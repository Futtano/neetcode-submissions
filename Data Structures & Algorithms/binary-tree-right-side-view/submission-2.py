# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # BFS Recursive solution
    # Time: O(n)
    # Space O(w), where w is the width of the tree
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res
        
        queue = deque([root])

        while queue:
            res.append(queue[0].val)
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return res


