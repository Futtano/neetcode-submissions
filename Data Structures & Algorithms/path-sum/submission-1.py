class Solution:
    # Check for a root-to-leaf path with the target sum
    # Let n be the number of nodes and h be the tree height.
    # Time complexity: O(n) worst case
    # Space complexity: O(h) auxiliary for the recursion stack
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], remaining: int) -> bool:
            if node is None:
                return False

            # Include this node in the path sum.
            remaining -= node.val

            # A path can satisfy the target only when it ends at a leaf.
            if node.left is None and node.right is None:
                return remaining == 0

            # A negative remainder can still match through a negative value.
            # Stop searching as soon as either subtree contains a valid path.
            return dfs(node.left, remaining) or dfs(node.right, remaining)

        return dfs(root, targetSum)