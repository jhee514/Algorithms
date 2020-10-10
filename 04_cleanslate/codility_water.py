def solution(N, K):
    pass


"""
There are N empty glasses with a capacity of 1, 2, .... , N liters
(there is exactly one glass of each unique capacity).
You want to pour exactly K liters of water into glasses.
Each glass may be either full or empty (a glass cannot be partially filled).
What is the minimum number of glasses that you need to contain K liters of water?
"""


def sol(n, k):
    flag = 0
    least = n
    water = k
    glasses = list(range(n, 0, -1))
    cnt = 0

    for i in range(n):
        if not water:
            break
        if water >= glasses[i]:
            flag = 1
            water -= glasses[i]
            cnt += 1

    if water:
        return -1
    if flag:
        return cnt
    else:
        return -1


"""
SKT_FE 02
"""