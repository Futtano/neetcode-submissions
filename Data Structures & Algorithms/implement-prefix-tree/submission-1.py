class TrieNode:
    def __init__(self):
        self.is_valid = False
        self.next = [None] * 26

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            next_idx = ord(c) - ord('a')
            if cur.next[next_idx] is None:
                cur.next[next_idx] = TrieNode()
            cur = cur.next[next_idx]

        cur.is_valid = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            next_idx = ord(c) - ord('a')
            if cur.next[next_idx] is None:
                return False
            cur = cur.next[next_idx]

        return cur.is_valid is True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            next_idx = ord(c) - ord('a')
            if cur.next[next_idx] is None:
                return False
            cur = cur.next[next_idx]

        return True
        
        