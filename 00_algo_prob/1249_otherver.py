import sys
sys.stdin = open("1249_input.txt", "r")

def sol(n, data):
    stack = [[0, 0]]
    visited = [[0] * n for _ in range(n)]
    memo = [[0] * n for _ in range(n)]


    visited[0][0] = 1
    """
    TODO
    이동하는 시간은 얼마 안걸린다는 전제 = > 비용이 적게 들면 돌아돌아가도 오케이,
    하지만 아무리 돌아가도 자기가 온 길은 돌아가면 안되겠지 
    그러니, 최단거리가 아닌 최소비용 문제로서, 
    깊이 우선 탐색으로 돌아온길만 제외하고 다 가보는 방법을 해야
    """
    while stack:
        cur = stack.pop(-1)
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for d in dir:
            yy, xx = cur[0] + d[0], cur[1] + d[1]
            if 0 <= yy < n and 0 <= xx < n and not visited[yy][xx]:
                stack.append([yy, xx])
                visited[yy][xx] = 1
                if memo[yy][xx] == 0 or memo[yy][xx] > memo[cur[0]][cur[1]] + data[yy][xx]:
                    memo[yy][xx] = memo[cur[0]][cur[1]] + data[yy][xx]
    return memo[n - 1][n - 1]


T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    print(sol(n, data))