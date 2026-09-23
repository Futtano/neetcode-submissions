class TrieNode:
    def __init__(self):
        self.next = [None] * 26
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        res = []

        self.insertWords(root, words)

        up, left =  -1, -1
        down, right = 1, 1
        lowYBound, lowXBound = 0, 0
        highYBound, highXBound = len(board)-1, len(board[0])-1

        def backtrack(y, x, board, cur: TrieNode):
            if y < lowYBound or y > highYBound or x < lowXBound or x > highXBound:
                return
            if board[y][x] == '#':
                return

            char = board[y][x]
            idx = ord(char) - ord('a')

            if cur.next[idx] is not None:
                cur = cur.next[idx]
                if cur.word is not None:
                    res.append(cur.word)
                    cur.word = None

                board[y][x] = '#'
                backtrack(y + up, x, board, cur)
                backtrack(y + down, x, board, cur)
                backtrack(y, x + left, board, cur)
                backtrack(y, x + right, board, cur)
            
            board[y][x] = char
            return

        for y in range(len(board)):
            for x in range(len(board[0])):
                backtrack(y, x, board, root)
        return res


    def insertWords(self, root: TrieNode, words: list[str]):
        for word in words:
            cur = root
            for ch in word:
                idx = ord(ch) - ord('a')
                if cur.next[idx] is None:
                    cur.next[idx] = TrieNode()
                cur = cur.next[idx]
            cur.word = word
    