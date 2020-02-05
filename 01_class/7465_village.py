import sys

sys.stdin = open("input_7465.txt", "r")


def find(x):
    for g in range(len(group)):
        if x in group[g]:
            return g
    return None


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(m)]

    group = []
    for d in data:
        if d[0] and d[1]:
            if find(d[0]) != None and find(d[1]) != None:
                if find(d[0]) != find(d[1]):
                    group[find(d[0])].update(group.pop(find(d[1])))
            elif find(d[0]) != None:
                group[find(d[0])].add(d[1])
            elif find(d[1]) != None:
                group[find(d[1])].add(d[0])
            else:
                group.append(set([d[0], d[1]]))
    cnt = 0
    people = list(range(1, n + 1))
    for p in people:
        if find(p) == None:
            cnt += 1
    print("#{} {}".format(tc + 1, cnt + len(group)))
