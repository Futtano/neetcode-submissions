class TrieNode:
    # Time: O(L) for each operation (insert, search and startsWith), where L is the word/prefix length
    # Space: O(n) more specifically O(26n), where n is the number of TrieNodes
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

        return cur.is_valid

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            next_idx = ord(c) - ord('a')
            if cur.next[next_idx] is None:
                return False
            cur = cur.next[next_idx]

        return True
        
        