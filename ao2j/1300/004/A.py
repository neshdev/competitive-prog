from dataclasses import dataclass

n = int(input())

@dataclass
class Card:
    """
    0 - spade
    1 - heart
    2 - clubs
    3 - diamond
    """
    suit: int
    num: int

    def scores(self):
        if self.num == 1:
            yield 1
            yield 11
        elif self.num in (11,12,13):
            yield 10
        else:
            yield self.num


cards = []
for s in ['S', 'H', 'C', 'D']:
    for num in range(1,14):
        c = Card(s, num)
        cards.append(c)

cards = [c for c in cards if not (c.num == 12 and c.suit == 'S')]
# print(cards)

total = 0
for c in cards:
    for score in c.scores():
        if 10 + score == n:
            total += 1

print(total)