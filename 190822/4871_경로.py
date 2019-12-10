import sys
sys.stdin = open("input_4871.txt", "r")


def isempty(list):
    if len(list) == 0:
        return 1
    else:
        return 0

def find(nodes):
    s = []
    visited = [0 for _ in range(total_nodes + 1)]
    curr = dep
    visited[curr] = 1
    while curr != arr:
        for i in range(total_paths):
            if paths[i][0] == curr:
                s.append(paths[i][1])

        if not isempty(s):
            curr = s[-1]
            visited[curr] = 1
            s.pop(-1)
        else:
            return 0
    return 1


T = int(input())
for tc in range(T):
    total_nodes, total_paths = map(int, input().split())
    paths = [list(map(int, input().split())) for _ in range(total_paths)]
    dep, arr = map(int, input().split())
    print("#%d %d" % (tc +1, find(paths)))