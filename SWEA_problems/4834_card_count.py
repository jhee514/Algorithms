import sys
sys.stdin = open("input_card.txt", "r")

# def find(n, cards):
#     card_count = {}
#     for card in cards:
#         card_count[card] = cards.count(card)
#     max_cards = [int(key) for key in card_count.keys() if card_count.get(key) == max(card_count.values()) ]
#     return (max(max_cards), max(card_count.values()))

def find(n, cards):
    maxNum = cards[0]
    maxCount = cards.count(cards[0])
    for i in range(1, n):
        if cards.count(cards[i]) > maxCount:
            maxNum = cards[i]
            maxCount = cards.count(cards[i])
        elif cards.count(cards[i]) == maxCount:
            if cards[i] > maxNum:
                maxNum = cards[i]
    return (int(maxNum), maxCount)

# sol.
# def find():
#     maxl = 0
#     for i in range(N):
#         num = int(v[i])
#         card[num] = card[num] + 1
#         if card[maxl] <= card[num]:  # 개수가 더 많은 숫자 카드 추가
#             maxl = max(maxl, num)
#         return maxl

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cards = list(input())
    # print("#%d %d %d" % (tc, find(cards)[0], find(cards)[1]))
    print("#%d %d %d" % (tc, find(n, cards)[0], find(n, cards)[1]))