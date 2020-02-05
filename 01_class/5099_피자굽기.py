import sys

sys.stdin = open("input_5099.txt", "r")


def find(cheese):
    q = []
    data = [i for i in range(num)]

    while len(q) != size:
        c = data.pop(0)
        q.append(c)
        cheese[c] = cheese[c] // 2

    while len(q) != 1:
        curr = q.pop(0)
        if cheese[curr] == 0:
            if data:
                next = data.pop(0)
                q.append(next)
                cheese[next] = cheese[next] // 2
        else:
            q.append(curr)
            cheese[curr] = cheese[curr] // 2
    return q[0] + 1


T = int(input())
for t in range(T):
    size, num = map(int, input().split())
    cheese = list(map(int, input().split()))
    print("#{} {}".format(t + 1, find(cheese)))