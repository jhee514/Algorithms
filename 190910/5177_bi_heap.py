import sys

sys.stdin = open("input_5177.txt", "r")

# 이진 완전 트리 => n : n*2, n*2 +1

def add_node(num):
    global cnt
    values[cnt] = num
    node = cnt
    while node//1 > 0 and values[node//2] > values[node]:
        values[node//2], values[node] = values[node], values[node//2]
        node = node//2


def sum_parent(node):
    total = 0
    while node > 0:
        total += values[node//2]
        node = node//2
    return total


T = int(input())
for tc in range(T):
    n = int(input())
    data = list(map(int, input().split()))

    values = [0] * (n+1)
    cnt = 0

    for i in data:
        cnt += 1
        add_node(i)

    print("#{} {}".format(tc+1, sum_parent(values.index(values[-1]))))