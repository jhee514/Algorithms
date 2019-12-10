import sys
sys.stdin = open("2117_input.txt", "r")

"""
서비스 지역이 도시 범위를 벗어나도 cost 는 변하지 않는다
각 가정 당 지불 비용이 M

손해 보지 않으면서 가장 많은 집들에 서비스 제공 가능한 영역크기 K를 찾고,
    0 <= K <= n 을 돌면서 확인
    
이 때 커버 되는 집들의 개수 출력
    dfs 의 depth 가 k 가 되는 것
"""
def in_town(a, b):
    if 0 <= a < n and 0 <= b < n:
        return True


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    max_cnt = 0
    for i in range(n):
        for j in range(n):
            for k in range(1, n+2):
                cost = (k*k) + (k-1)*(k-1)
                cnt = 0
                for kk in range(k):
                    if kk == 0:
                        y = i
                        for x in range(j - k + 1 + kk, j + k - kk):
                            if in_town(y, x) and data[y][x]:
                                cnt += 1
                    else:
                        y = i - kk
                        for x in range(j - k + 1 + kk, j + k - kk):
                            if in_town(y, x) and data[y][x]:
                                cnt += 1
                        y = i + kk
                        for x in range(j - k + 1 + kk, j + k - kk):
                            if in_town(y, x) and data[y][x]:
                                cnt += 1
                if cost <= cnt * m and cnt > max_cnt:
                    max_cnt = cnt
    print("#{} {}".format(tc+1, max_cnt))