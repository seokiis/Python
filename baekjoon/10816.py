# 10
# 6 3 2 10 10 10 -10 -10 7 3
# -10 -10 2 3 3 6 7 10 10 10
# 8
# 10 9 -5 2 3 4 5 -10

import sys

input = sys.stdin.readline


n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
my_cards = list(map(int, input().split()))


def binary_search(start, end, ob):
    if start > end:
        return 0
    m = (start + end) // 2
    if cards[m] == ob:
        return cards[start : end + 1].count(ob)
    elif cards[m] > ob:
        return binary_search(start, m - 1, ob)
    elif cards[m] < ob:
        return binary_search(m + 1, end, ob)


answer = {}
for card in my_cards:
    if card not in answer:
        answer[card] = binary_search(0, len(cards) - 1, card)

for card in my_cards:
    print(answer[card], end=" ")
