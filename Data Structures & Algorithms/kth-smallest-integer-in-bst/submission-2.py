# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Inorder traversal for ascending order, 
    # with counter of popped nodes
    # Let h be the height of the tree and k be the number of popped
    # nodes from the stack
    # Time complexity: O(h + k)
    # Space complexity: O(h)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root

        while current or stack:
            if current is None:
                # Leftmost node, pop and decrement k
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                # Try the right subtree
                current = node.right
            else:
                # Descend the all the left subtree
                stack.append(current)
                current = current.left

        # k is guaranteed to be  <= number of nodes so this 
        # will never execute
        return -1