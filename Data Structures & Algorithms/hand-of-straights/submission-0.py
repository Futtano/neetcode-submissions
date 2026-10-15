class Solution:
    # Time: O(nlogn)
    # Space: O(n)
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = {}
        for card in hand:
            freq[card] = freq.get(card, 0) + 1

        hand.sort()

        for x in hand:
            if freq[x] == 0:
                continue

            for card in range(x, x + groupSize):
                if freq.get(card, 0) == 0:
                    return False
                freq[card] -= 1

        return True