class Solution:
    # Compute the diameter with a postorder DFS.
    # Let n be the number of nodes and h be the tree height.
    # Time complexity: O(n)
    # Space complexity: O(h) auxiliary for the recursion stack
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def height(node: Optional[TreeNode]) -> int:
            nonlocal best

            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            # Each child height equals the number of edges from this
            # node down that side, including the edge to the child.
            best = max(best, left_height + right_height)

            # A downward path can continue through only one child.
            return 1 + max(left_height, right_height)

        height(root)
        return best