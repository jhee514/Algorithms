import sys
sys.stdin = open('16234_input.txt', 'r')


for tc in range(5):
    n, l, r = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    cnt = 0
    while 1:
        flag = False
        visited = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                # visited 안한 모든 칸을 dfs 로 검
                if not visited[i][j]:
                    q = [[i, j]]
                    visited[i][j] = 1
                    tmp_total_popul = data[i][j]
                    tmp_union = [[i, j]]
                    while q:
                        cur = q.pop(0)
                        for dir in directions:
                            y, x = cur[0] + dir[0], cur[1] + dir[1]
                            if 0<=y<n and 0<=x<n and not visited[y][x] and l <= abs(data[cur[0]][cur[1]] - data[y][x]) <= r:
                                # 인구이동을 할 수 있는 연합할 국가가 있을 때 flag 를 변화
                                flag = True
                                visited[y][x] = 1
                                q.append([y, x])
                                tmp_total_popul += data[y][x]
                                tmp_union.append([y, x])
                    # 연합할 국가가 있을 때
                    if flag:
                        tmp_avg_popul = tmp_total_popul // len(tmp_union)
                        for u in tmp_union:
                            data[u[0]][u[1]] = tmp_avg_popul
        # 더이상 연합할 국가들이 없을 때
        if not flag:
            break
        # flag 가 true 면 인구이동을 했다는
        else:
            cnt += 1
    print(cnt)

# 120348 kb
# 1060 ms
