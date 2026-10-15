class Solution:
    # BFS
    # Let N=len(wordList) and L=len(beginWord)
    # Time: O(N^2 * L)
    # Space: O(N)
    def ladderLength(self, beginWord, endWord, wordList):
        remaining = set(wordList)
        if endWord not in remaining:
            return 0

        queue = deque([(beginWord, 1)])
        remaining.discard(beginWord)

        while queue:
            word, length = queue.popleft()

            for candidate in list(remaining):
                differences = sum(
                    a != b for a, b in zip(word, candidate)
                )
                if differences != 1:
                    continue

                if candidate == endWord:
                    return length + 1

                remaining.remove(candidate)
                queue.append((candidate, length + 1))

        return 0