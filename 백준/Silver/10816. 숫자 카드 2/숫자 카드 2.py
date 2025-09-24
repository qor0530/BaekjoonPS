from collections import defaultdict

n = int(input())

card = list(input().split())

cards = defaultdict(int)

for c in card:
    cards[c] += 1

m = int(input())

show = list(input().split())

for s in show:
    print(cards[s], end=' ')