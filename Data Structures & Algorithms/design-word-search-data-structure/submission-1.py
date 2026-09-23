class TrieNode:
    def __init__(self):
        self.isValid = False
        self.next = [None] * 26

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if cur.next[idx] is None:
                cur.next[idx] = TrieNode()
            cur = cur.next[idx]
        cur.isValid = True

    def search(self, word: str) -> bool:
        def findSubWord(node: TrieNode, subWord:str) -> bool:
            cur = node
            for i, ch in enumerate(subWord):
                if ch != '.':
                    idx = ord(ch) - ord('a')
                    if cur.next[idx] is None:
                        return False
                    cur = cur.next[idx]
                else:
                    found = False
                    for children in cur.next:
                        if children is not None:
                            found = found or findSubWord(children, subWord[i+1:])
                            if found:
                                return True
                    return False

            return cur.isValid

        return findSubWord(self.root, word)