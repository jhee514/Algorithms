import sys

sys.stdin = open("17144_input.txt", "r")

"""
청정기 => 2칸 차지, 가장 왼열에 위치
미세먼지 확산 : 인접한 네방향으로 확산
    인접한 곳에 청정기 / 벽 있으면 확산 안함
    확산 양은 원래의 dust(r, c)//5
    원래 칸은 d - d//5*확산방향개수
청정기(-1) => 위 : 반시계방향 순환
        아래 : 시계방향 순환
        바람 => 미세먼지가 바람의 방향대로 모두 한칸씩 이동
        공기청정기에 들어간 미세먼지는 모두 정화된다.
        
        위칸 청정기
            col==0: row 의 range(0, pur[0]-1) 까지 각각의 값을 row+1 씩 이동 시켜 값을 덮어씌
        아래칸 청정기
            col=0: row in range(r-1, pur[1]-1, -1) 각각의 값을 row-1 씩 이동시켜 값을 덮어
        row == 0, r-1 에 있는 값들을 col in range(c-1, 0, -1) 해서 각각의 값을 col-1 씩 이동, 값을 덮어
        위칸 청정기
            col==c-1: row in range(pur[0], 0, -1) 각 값을 row-1 씩 이동, 값 덮어
        아래칸 청정기
            col==c-1: row in range(pur[1], c) 각 값을 row+1 씩 이동, 값 덮
        data[pur[0]][1] = 0
        data[pur[1]][1] = 0  
"""

"""
1. 미세먼지 찾기 함수
    리스트에 각 미세먼지 위치를 넣는다
2. 미세먼지 확산 함수
    q 에 더스트 위치를 다 넣고
    각각의 더스트 위치를 돌면서
        arr = [[0]*c for r] (여기다 새로 갱신되는 더스트 값을 넣어야)
        각 더스트 위치 arr 의 사방 += 해당 더스트 양의 //5
        그리고 해당 더스트는 arr[더스트위치] += d - (d//5*확산방향개수)
        이 arr 를 return 한다
3. 공기청정기 작동
    인덱싱을 잘해주
"""


# dust 가 있는 칸의 위치를 검색
# dusts = [[y1, x1], [y2, x2], ...] 형태로 받는다
def find_dust(r, c, data):
    dusts = []
    for i in range(r):
        for j in range(c):
            if data[i][j] > 0:
                dusts.append([i, j])
    return dusts


# 공기청정기 위치를 검색
# 항상 제일 왼쪽 col==0 에 위치하니까 두개의 연속된 row 값만 list 에 저장
def find_purifier(r, c, data):
    for i in range(r):
        if data[i][0] == -1:
            purifiers = [i, i + 1]
            return purifiers


# 미세먼지 확산 후 미세먼지 양을 계산
def spread_dust(r, c, data, purifiers):
    dusts = find_dust(r, c, data)
    # 미세먼지 값을 기존의 array 에 덮어 씌우면 다음 미세먼지 확산을 계산할 수 없어
    # 새로운 array 를 spreaded 로 명명, 0 으로 채워 넣어 새로 만들어서 여기에 새로 계산된 미세먼지 값을 입력한
    spreaded = [[0] * c for _ in range(r)]
    # 공기 청정기 자리는 -1 로 채워 넣기
    spreaded[purifiers[0]][0] = -1
    spreaded[purifiers[1]][0] = -1
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # find_dust 함수를 통해 찾은 미세먼지 위치를 for 문을 이용해 탐색하며 사방으로 벽 또는 공기청정기 아닌 곳으로 확산시켜준다
    for dust in dusts:
        # 4방향 중 몇 군데로 미세먼지가 퍼져 나가는지 count
        cnt_spreaded = 0
        for dir in directions:
            near = [dust[0] + dir[0], dust[1] + dir[1]]
            if near != [purifiers[0], 0] and near != [purifiers[1], 0] and 0 <= near[0] < r and 0 <= near[1] < c:
                # 한 칸에서 여러개(?)의 미세먼지를 받을 수 있으니까 = 가 아닌 += 를 이용
                spreaded[near[0]][near[1]] += data[dust[0]][dust[1]] // 5
                # 퍼져 나갈 때마다 count += 1
                cnt_spreaded += 1
        # 퍼져 나간 미세먼지 양만큼 뺀 값을 기존의 dust 칸에 더해준
        spreaded[dust[0]][dust[1]] += data[dust[0]][dust[1]] - (data[dust[0]][dust[1]] // 5 * cnt_spreaded)
    return spreaded


# 공기 청정기 틀고 난 후 미세먼지 위치 조정
# 공기청정기로 들어오는 미세먼지 칸 부터 공기청정기 바람이 나오는 방향(역순)으 값을 계산해준다
def air_purified(r, c, data, purifiers):
    # 윗칸 공기청정기 ↓ 방향
    for row in range(purifiers[0] - 2, -1, -1):
        data[row + 1][0] = data[row][0]
    # 아래 청정기 ↑ 방향
    for row in range(purifiers[1] + 2, r):
        data[row - 1][0] = data[row][0]
    for col in range(1, c):
        # 윗칸 공기청정기 ← 방향
        data[0][col - 1] = data[0][col]
        # 아래 청정기 ← 방향
        data[r - 1][col - 1] = data[r - 1][col]
    # 윗칸 청정기 ↑ 방향
    for row in range(1, purifiers[0] + 1):
        data[row - 1][c - 1] = data[row][c - 1]
    # 아래 청정기 ↓ 방향
    for row in range(r - 2, purifiers[1] - 1, -1):
        data[row + 1][c - 1] = data[row][c - 1]
    # 위아래 청정기 → 방
    for col in range(c - 2, 0, -1):
        data[purifiers[0]][col + 1] = data[purifiers[0]][col]
        data[purifiers[1]][col + 1] = data[purifiers[1]][col]향
    # 청정기 오른편 칸 공기 정화
    data[purifiers[0]][1] = 0
    data[purifiers[1]][1] = 0

# dust 합 구하기
def sum_dusts(r, c, data):
    total = 0
    for i in range(r):
        for j in range(c):
            if data[i][j] > 0:
                total += data[i][j]
    return total


T = 8
for _ in range(T):
    r, c, t = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(r)]
purifiers = find_purifier(r, c, data)
# t 초 동안 미세먼지 확산 + 공기 청정 t 번 하기
while t:
    # spreaded 에 확산된 후의 미세먼지 양을 계산
    spreaded = spread_dust(r, c, data, purifiers)
    # 위에서 계산한 미세먼지를 청정
    air_purified(r, c, spreaded, purifiers)
    # 다시한번 이 과정을 반복하기 위해 data 에 청정된 후의 미세먼지 값으로 재할당
    data = spreaded
    # 카운팅 깎아주기
    t -= 1
# while 문 끝나면 미세먼지 합 구하기
print(sum_dusts(r, c, data))


"""
재평 code
=> is_wall 을 활용하여서 청정기 도는 함수도 is_wall 일 때마다 방향을 바꿔 주도록 해주면 하드 코딩이 줄겠죠!!!
"""