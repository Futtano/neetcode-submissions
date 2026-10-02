class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        notSegmentable = set()
        segmentable = set()
        wordDict.sort()
        def isSegmentable(start: int, end: int) -> bool:
            if start >= end:
                return True
            if s[start: end] in notSegmentable:
                return False
            if s[start: end] in segmentable:
                return True

            for word in wordDict:
                relStart = s[start: end].find(word)
                if relStart != -1:
                    subStart = start + relStart
                    subEnd = subStart + len(word)
                    found = (
                        isSegmentable(subEnd, end) and
                        isSegmentable(start, subStart)
                    )
                    if found:
                        segmentable.add(s[subStart: subEnd])
                        return True

            notSegmentable.add(s[start: end])
            return False

        return isSegmentable(0, len(s))