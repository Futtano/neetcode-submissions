# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    # Preorder DFS approach with implicit stack
    # Time: O(n)
    # Space: O(n)
    def serialize(self, root):
        vals = []

        def dfs(node):
            if node is None:
                vals.append("#")
                return

            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    # Time: O(n)
    # Space: O(n)
    def deserialize(self, data):
        vals = iter(data.split(","))

        def dfs():
            val = next(vals)

            if val == "#":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()