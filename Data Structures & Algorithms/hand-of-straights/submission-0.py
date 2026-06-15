class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        cards = [[] for _ in range(len(hand)//groupSize)]

        for num in hand:
            added = False
            for card in cards:
                if not card or (card[-1] + 1 == num and len(card) < groupSize):
                    card.append(num)
                    added = True
                    break

            if not added:
                return False

        return True