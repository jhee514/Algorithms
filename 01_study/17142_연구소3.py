import sys
sys.stdin = open("17142_input.txt", "r")

"""
1-1 바이러스 위치(1) 뽑아 내고 (value 가 2)
    1-2 그 중 세개 조합 뽑고
        하드카피?
        list not in
    1-3 - 거기서부터 visited 를 1 씩 해서다
2-1 bfs 로 이동
    * 이 떄 세개의 virus 가 동시에 이동해야해!!!*
    * virus_1 virus_2 virus_3 *
     2-2 비활성 바이러스() 만나면 바이러스가 비활성태로
     2-3 벽(value 가 1) 만나면 바이러스가 비활성상태로
    2-4 value 가 0 이면 한칸 이동 때마다 cur_visitied + 1 로 잡아주고
    2-5 목적지에 도착시 min_distance max_visited 비
3-1 결과 출력
    3-2 0 이 존재하면 -1 을 출력
    3-3 else 면 max_visited - active_virus + 1 을 해준
"""



def find_virus(data):
    viruses = []
    for i in range(n):
        for j in range(n):
            if data[i][j] == 2:
                viruses.append([i, j])
    return viruses

def has_zero(data, n):
    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                return True
    return False

def dfs(arr, m): # arr = [[i, j], [i, j],[i, j] ...]
    global min_time
    q = [0] * n * n
    front, rear = -1, -1
    visited = [[0] * n for _ in range(n)]
    # visited 를 카피 대신 활용
    # data[i][j] == 1 or 2; visited == 1

    for i in range(m):
        rear += 1
        q[rear] = arr[i]
        visited[arr[i][0]][arr[i][1]] = 2

    dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    while front != rear:
        front += 1
        cur = q[front]
        for d in range(4):
            y, x = cur[0] + dir[d][0], cur[1] + dir[d][1]
            if 0 <= y < n and 0 <= x < n and not visited[y][x]:
                if data[y][x] == 0:
                    rear += 1
                    q[rear] = [y, x]
                    visited[y][x] = visited[cur[0]][cur[1]] + 1
                elif data[y][x] == 1 or data[y][x] == 2:
                    visited[y][x] = 2
    if not has_zero(visited, n) and max(map(max, visited)) - 2 < min_time:
        min_time = max(map(max, visited)) - 2



def comb_virus(arr, temp, r, n):
    # 조합을 리스트의 인덱싱으로 구성
    if r == 0:
        dfs(temp, m)
    elif n < r:
        return False
    else:
        temp[r-1] = arr[n-1]
        comb_virus(arr, temp, r-1, n-1)
        comb_virus(arr, temp, r, n-1)


for tc in range(7):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    if not has_zero(data, n):
        print(0)
    else:
        min_time = n*n*n
        viruses = find_virus(data)
        active_viruses = [0] * m
        comb_virus(viruses, active_viruses, m, len(viruses))
        flag = False
        if min_time != n*n*n:
            print(min_time)
        else:
            print(-1)
