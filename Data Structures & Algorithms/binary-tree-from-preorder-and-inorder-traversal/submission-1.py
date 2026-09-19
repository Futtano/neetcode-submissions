# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(n)
    # Space: O(n)
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[TreeNode]:

        positions = {value: i for i, value in enumerate(inorder)}

        def dfs(l, r, pre_idx):
            if l > r:
                return None

            root_val = preorder[pre_idx]
            i = positions[root_val]

            node = TreeNode(root_val)

            left_size = i - l

            node.left = dfs(l, i - 1, pre_idx + 1)
            node.right = dfs(
                i + 1,
                r,
                pre_idx + 1 + left_size
            )

            return node

        return dfs(0, len(inorder) - 1, 0)