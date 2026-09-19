# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    # Time: O(n)
    # Space: O(n)
    def serialize(self, root):
        if root is None:
            return ''

        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                res.append('.')
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ','.join(res)
    
        
    # Decodes your encoded data to tree.
    # Time: O(n)
    # Space: O(n)
    def deserialize(self, data):
        if not data:
            return None

        values = data.split(',')

        root = TreeNode(int(values[0]))
        queue = deque([root])

        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            # left child
            if i < len(values) and values[i] != '.':
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)

            i += 1

            # right child
            if i < len(values) and values[i] != '.':
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)

            i += 1

        return root
            



