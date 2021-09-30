figures = {
    "Jack": 11,
    "King": 13,
    "Queen": 12,
    "Ace": 14,
}

cards = []
for _i in range(6):
    cards.append(input())

sum_ = 0
value = 0
for card in cards:
    try:
        value = int(card)
    except ValueError:
        value = figures.get(card)
    sum_ += value

print(sum_ / 6)
