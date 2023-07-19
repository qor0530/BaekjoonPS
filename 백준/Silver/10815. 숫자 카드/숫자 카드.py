import bisect
N = int(input())
number_card = list(map(int, input().split()))
number_card.sort()

M = int(input())
card_list = list(map(int, input().split()))
for card in card_list:
    if (bisect.bisect_right(number_card, card) - bisect.bisect_left(number_card, card)) == 1:
        print(1, end=' ')
    else:
        print(0, end=' ')