import sys
sys.stdin = open("1932_input.txt", "r")

"""
bfs
자신의 row 전후에 있는 row 들에 있는 값들 가운데
자신의 인덱스(i) 값과 같은 값을 갖거나 1 큰 인덱스를 갖는 애들이 후보
but 후보가 될 수 있는 index 의 range 가 중요
    len(data[j]) == j
    
visited 처리를 3차원 배열로 [boolean, depth, sum]으로 가져가보자 

q 를 이용하여 도는데, 이 때 종료 시점은 depth 가 n-1 일 때이다 => 시작 depth 는 0이다
"""

"""
왜 이걸 bfs 라고 생각했는지는 모르겠다
하지만 이 문제는 dfs로 접근해야한다.
최단 경로를 찾는 것이 아니라 끝까지 가봐야 답을 비교할 수 있기 때문.
이 문제의 경우 동서남북 네방향이 아닌 해당 숫자의 바로 아래행의 같은 열 또는 +1 열로만 이동 가능하기 때문에
visited 처리를 따로 해주지 않아도 된다.
"""

def in_range(i, j, k):
    if 0 <= i < k and 0 <= j < i + 1:
        return True
    else:
        return False


def sol(n, data):
    s = [[0, 0]]
    visited = [list([0, 0, 0] for _ in range(i+1)) for i in range(n)]
    visited[0][0] = [1, 0, data[0][0]]
    max_dist = 0
    dir = [[1, 0], [1, 1]]
    while s:
        cur = s.pop(-1)
        for d in dir:
            dy, dx = cur[0] + d[0], cur[1] + d[1]
            if in_range(dy, dx, n):
                s.append([dy, dx])
                visited[dy][dx] = [1, dy, visited[cur[0]][cur[1]][2] + data[dy][dx]]
                if visited[dy][dx][1] == n - 1 and visited[dy][dx][2] > max_dist:
                    max_dist = visited[dy][dx][2]
    return max_dist


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
print(sol(n, data))