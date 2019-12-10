import sys

sys.stdin = open("input_5174.txt", "r")


def postorder(node):
    global cnt
    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        cnt += 1


T = int(input())
for tc in range(T):
    e, n = map(int, input().split())
    data = list(map(int, input().split()))
    nums = [data[i * 2:(i + 1) * 2] for i in range(e)]

    tree = [[0] * 2 for _ in range(e + 2)]
    for j in nums:
        p, c = j[0], j[1]
        if tree[p][0]:
            tree[p][1] = c
        else:
            tree[p][0] = c

    cnt = 0
    postorder(n)
    print("#{} {}".format(tc + 1, cnt))