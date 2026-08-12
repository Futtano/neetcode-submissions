class Solution:
    # Frequency-based encoding
    # Note: Python dict preserve insertion order from 3.7+
    def encode(self, strs: List[str]) -> str:
        return ''.join(
            f"{len(s)}#{s}" for s in strs
        )

    def decode(self, s: str) -> List[str]:
        start = 0
        result = []
        while start < len(s):
            end = start

            while s[end] != '#':
                end += 1

            length = int(s[start: end])
            str_start = end + 1
            result.append(s[str_start: str_start + length])
            start = str_start + length

        return result

