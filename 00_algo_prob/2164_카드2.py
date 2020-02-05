"""
1 2 3 4 5 6
2 3 4 5 6
3 4 5 6 2
4 5 6 2
5 6 2 4
6 2 4
2 4 6
4 6
6 4
4
"""
from collections import deque
n = int(input())
card = deque(range(1, n+1))
while len(card) > 1:
    card.popleft()
    card.append(card.popleft())
print(card[0])