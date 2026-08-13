class Solution:
    # Frequency-based encoding
    # Note: Python dict preserve insertion order from 3.7+
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return '-1'

        freq_list= []
        for s in strs:
            freq = {}
            for ch in s:
                freq[ch] = 1 + freq.get(ch, 0)
            freq_list.append(freq)

        encoded_list = list(map(
            lambda freq: ''.join(
                f"{v}{k}" for k,v in freq.items() 
            ), freq_list
        ))
        encoded = '-'.join(encoded_list)
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == '-1':
            return []

        decoded_list = s.split('-')
        result = []
        for item in decoded_list:
            decoded = "".join(
                f"{item[i+1]}" * int(item[i])
                for i in range(0, len(item), 2)
            )
            result.append(decoded)

        return result
