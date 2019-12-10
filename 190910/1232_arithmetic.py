import sys

sys.stdin = open("input_1232.txt", "r")

# TODO tree 에 그냥 바로 요소 값을 저장하면 더 간단해진다

def arithmetic(node):
    lc, rc = tree[node][0], tree[node][1]
    if node:
        arithmetic(lc)
        arithmetic(rc)
        if values[node] == '+':
            values[node] = values[lc] + values[rc]
        elif values[node] == '-':
            values[node] = values[lc] - values[rc]
        elif values[node] == '/':
            values[node] = values[lc] // values[rc]
        elif values[node] == '*':
            values[node] = values[lc] * values[rc]


T = 10
for tc in range(T):
    n = int(input())
    data = [list(input().split()) for _ in range(n)]

    tree = [[0] * 2 for _ in range(n + 1)]
    values = [0] * (n + 1)

    for i in data:
        if len(i) > 3:
            node, val, lc, rc = int(i[0]), i[1], int(i[2]), int(i[3])
            values[node] = val
            tree[node][0], tree[node][1] = lc, rc
        elif len(i) < 3:
            node, val = int(i[0]), int(i[1])
            values[node] = val
    arithmetic(1)
    print("#{} {}".format(tc + 1, values[1]))

###########################################################################

def arithmetic(node):
    lc, rc = tree[node][0], tree[node][1]
    if node:
        arithmetic(lc)
        arithmetic(rc)
        if values[node] == '+':
            values[node] = values[lc] + values[rc]
        elif values[node] == '-':
            values[node] = values[lc] - values[rc]
        elif values[node] == '/':
            values[node] = values[lc] // values[rc]
        elif values[node] == '*':
            values[node] = values[lc] * values[rc]


T = 10
for tc in range(T):
    n = int(input())
    data = [list(input().split()) for _ in range(n)]

    tree = [[0] * 2 for _ in range(n + 1)]
    values = [0] * (n + 1)

    for i in data:
        if len(i) > 3:
            node, val, lc, rc = int(i[0]), i[1], int(i[2]), int(i[3])
            values[node] = val
            tree[node][0], tree[node][1] = lc, rc
        elif len(i) < 3:
            node, val = int(i[0]), int(i[1])
            values[node] = val
    arithmetic(1)
    print("#{} {}".format(tc + 1, values[1]))