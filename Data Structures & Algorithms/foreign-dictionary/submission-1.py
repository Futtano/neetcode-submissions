class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        result = []
        unique_chars = set(c for w in words for c in w)
        in_deg = [None] * 26
        adj = defaultdict(set)
        for ch in unique_chars:
            in_deg[ord(ch) - ord('a')] = 0

        for w1, w2 in zip(words[:-1], words[1:]):
            i = j = 0
            while i < len(w1) and j < len(w2):
                if  w1[i] != w2[j]:
                    break
                i += 1
                j += 1
                
            # substring case, if j reached the end
            # of w2 first, it is a substring of w1
            # but comes after, return """
            if j == len(w2) and i < len(w1):
                return ""
            # valid subtring
            if i == len(w1) and j <= len(w2):
                continue

            # add the edge
            if w2[j] not in adj[w1[i]]:
                adj[w1[i]].add(w2[j])
                # increase in-degree of w2[j]
                idx = ord(w2[j]) - ord('a')
                in_deg[idx] += 1


        queue = deque(
            i for i in range(len(in_deg)) if in_deg[i] is not None and in_deg[i] == 0
            )

        while queue:
            idx = queue.popleft()
            # transform back to char and append to result
            ch = chr(idx + ord('a'))
            result.append(ch)

            # decrease affected nodes' in-degrees
            # and add them to the queue if their
            # count is zero
            for n in adj[ch]:
                pos = ord(n) - ord('a')
                in_deg[pos] -= 1
                if in_deg[pos] == 0:
                    queue.append(pos)


        return "".join(result) if len(unique_chars) == len(result) else ""