class Solution:
    # Check for a root-to-leaf path sum using an explicit DFS stack
    # Let n be the number of nodes and h be the tree height.
    # Time complexity: O(n) worst case
    # Space complexity: O(h) auxiliary, with O(1) on a chain
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        # Each entry carries the sum still needed before including its node.
        stack = [(root, targetSum)]

        while stack:
            node, remaining = stack.pop()
            remaining -= node.val

            if node.left is None and node.right is None and remaining == 0:
                return True

            # Push right first so the left child is popped first.
            if node.right is not None:
                stack.append((node.right, remaining))
            if node.left is not None:
                stack.append((node.left, remaining))

        return False