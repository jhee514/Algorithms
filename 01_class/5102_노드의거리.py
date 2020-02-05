import sys

sys.stdin = open("input_5102.txt", "r")


def find():
    q = []
    visited = [0] * (node + 1)

    q.append(dep)
    while q:
        curr = q.pop(0)
        for i in range(total_paths):
            if paths[i][0] == curr and not visited[paths[i][1]]:
                q.append(paths[i][1])
                visited[paths[i][1]] += visited[curr] + 1
                if paths[i][1] == arr:
                    return visited[paths[i][1]]
            if paths[i][1] == curr and not visited[paths[i][0]]:
                q.append(paths[i][0])
                visited[paths[i][0]] += visited[curr] + 1
                if paths[i][0] == arr:
                    return visited[paths[i][0]]
    return 0

T = int(input())
for t in range(T):
    node, total_paths = map(int, input().split())
    paths = [list(map(int, input().split())) for _ in range(total_paths)]
    dep, arr = map(int, input().split())
    print("#{} {}".format(t + 1, find()))
    print(node, total_paths, paths, dep, arr)