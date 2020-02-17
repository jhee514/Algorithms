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

def in_range(i, j, k):
    if 0 <= i < k and 0 <= j < k:
        return True
    else:
        return False


def sol(n, data):
    q = [[0, 0]]
    visited = [list([0, 0, 0] for _ in range(i+1)) for i in range(n)]
    visited[0][0] = [1, 0, data[0][0]]
    max_dist = 0
    dir = [[1, 0], [1, 1]]

    while q:
        cur = q.pop(0)
        for d in dir:
            dy, dx = cur[0] + d[0], cur[1] + d[1]
            if not visited[dy][dx][0]:
                if in_range(dy, dx, n):
                    q.append([dy, dx])
                    visited[dy][dx] = [1, visited[cur[0]][cur[1]][1] + 1, visited[cur[0]][cur[1]][2] + data[dy][dx]]
                    if visited[dy][dx][1] == n-1 and visited[dy][dx][2] > max_dist:
                        max_dist = visited[dy][dx][2]
    return max_dist


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
print(sol(n, data))