import sys
sys.stdin = open("input_5249.txt", "r")

"""
1. 간선이 하나인 애들은 무조건 연결
2. 간선이 여럿인 애들
    not visited 인 애들 중에서 골라서 연
"""
#
# T = int(input())
# for tc in range(T):
#     v, e = map(int, input().split())
#     data = [[0] for _ in range(v + 1)]
#     for _ in range(e):
#         a, b, c, = map(int, input().split())
#         if not data[a][0]:
#             data[a][0] = [b, c]
#         else:
#             data[a].append([b, c])
#
#         if not data[b][0]:
#             data[b][0] = [a, c]
#         else:
#             data[b].append([a,c])
#     print(data)

################################################
def find(x):
    for g in range(len(group)):
        if x in group[g]:
            return g
    return None

T = int(input())
for tc in range(T):
    v, e = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(e)]

    visited = [0] * (v+1)
    cnt = 0

    data.sort(key=lambda x:x[2])

    group = []
    for d in data:
        if visited[d[0]] and visited[d[1]]:
            if find(d[0]) != find(d[1]):
                group[find(d[0])].update(group.pop(find(d[1])))
                cnt += d[2]
        elif not visited[d[0]] and not visited[d[1]]:
            visited[d[0]] = 1
            visited[d[1]] = 1
            group.append(set([d[0], d[1]]))
            cnt += d[2]
        elif not visited[d[0]]:
            visited[d[0]] = 1
            group[find(d[1])].add(d[0])
            cnt += d[2]
        elif not visited[d[1]]:
            visited[d[1]] = 1
            group[find(d[0])].add(d[1])
            cnt += d[2]
    print("#{} {}".format(tc+1, cnt))