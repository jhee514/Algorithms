import sys

sys.stdin = open("input_5122.txt", "r")


def change(n1, num):
    q.pop(n1)
    q.insert(n1, num)


def insertion(i1, num):
    q.insert(i1, num)


def deletion(i):
    q.pop(i)


def find():
    for order in orders:
        if order[0] == "C":
            change(int(order[1]), int(order[2]))
        if order[0] == "I":
            insertion(int(order[1]), int(order[2]))
        if order[0] == "D":
            deletion(int(order[1]))
    if len(q) > l:
        return q[l]
    else:
        return -1


T = int(input())
for tc in range(T):
    n, m, l = map(int, input().split())
    q = list(map(int, input().split()))
    orders = [list(input().split()) for _ in range(m)]
    print("#{} {}".format(tc + 1, find()))
