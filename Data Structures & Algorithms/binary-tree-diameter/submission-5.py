class Solution:
    # Compute the diameter with iterative postorder DFS.
    # Let n be the number of nodes and h be the tree height.
    # Time complexity: O(n), assuming constant-time dictionary operations
    # Space complexity: O(h) auxiliary
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        best = 0
        heights = {}
        stack = [(root, False)]

        while stack:
            node, ready = stack.pop()

            if not ready:
                # Process this node after both children.
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
                continue

            # Each child's height is used once, by its parent.
            # A missing child contributes zero.
            left_height = heights.pop(node.left, 0)
            right_height = heights.pop(node.right, 0)

            best = max(best, left_height + right_height)
            heights[node] = 1 + max(left_height, right_height)

        return best