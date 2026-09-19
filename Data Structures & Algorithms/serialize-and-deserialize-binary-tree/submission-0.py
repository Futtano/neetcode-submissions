# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        if root is None:
            return ''

        queue = deque([root])
        while queue:
            el = queue.popleft()
            res.append(el)
            if el:
                queue.append(el.left)
                queue.append(el.right)

        return','.join('.' if i is None else str(i.val) for i in res)
    
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if str == '':
            return None
        nodeList = data.split(',')
        i = 1
        end = len(nodeList)
        root = TreeNode(nodeList[0])
        queue = deque([root])
        while queue and i < end:
            node = queue.popleft()
            if i < end and nodeList[i] != '.':
                newLeft = TreeNode(nodeList[i])
                queue.append(newLeft)
                node.left = newLeft
            if i < end and nodeList[i+1] != '.':
                newRight = TreeNode(nodeList[i+1])
                queue.append(newRight)
                node.right = newRight
            i += 2

        return root
            



