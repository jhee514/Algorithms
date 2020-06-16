import sys
sys.stdin = open("5653_input.txt", "r")

"""
세포당 [is_active, life, left_hours]로 값을 저장한다.
before, after table을 따로 관

0. 빈자리 0, 0, 0

1. 죽은 상태 is_active == -1 => nth

2. 활성상태 is_active == 1, life, left_hours는 life부터 시작
    시간이 지날 때마다 left -= 1
        => left 가 0이면 is_active = 0
        => life == left:ㅍ 복제
        => else: nth
    
3. 비활성 상태 is_active == 0, life >0인 상태
    시간 지날 때마다 left -= 1
    => if left == 0:
        is_active = 1, left = life
    => else: nth
        
        
싸이클
준비
1시간 지남
비활성 -> 활성 인 애들 찾아서 바꾸기
활성 -> 죽은 애들 바꾸기
번식
"""
def count_alive(n, m, data):
    cnt = 0
    for i in range(n):
        for j in range(m):
            cell = data[i][j]
            if cell[0] > -1 and cell[1] > 0:
                cnt += 1
    return cnt


def set_data(n, m, k, data):
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = [0, 0, 0]
            else:
                data[i][j] = [0, data[i][j], data[i][j]]

    bigger_dish = [[[0, 0, 0]] * (m+2*k) for _ in range(n+2*k)]
    for i in range(n):
        for j in range(m):
            bigger_dish[i+k][j+k] = data[i][j]
    return bigger_dish


def hour_passed(n, m, k, data):
    for i in range(n):
        for j in range(m):
            if data[i][j][0] > -1 and data[i][j][1] > 0:
                data[i][j][2] -= 1
    return data


def prolifer(i, j, n, m, k, data, after):
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for d in dir:
        y, x = i + d[0], j + d[1]
        # 새로 증식할 자리가 빈자리일 떄
        if after[y][x] == [0, 0, 0]:
            after[y][x] = [0, data[i][j][1], data[i][j][1]]
        # 새로 증식할 자리가 죽은자리 일 때
            # pass
        # 새로 증식할 자리가 비활성상태 / 활성 상태 일 떄
            # pass
        # 새로 증식할 자리가 새로 증식된 자리일 때
        elif after[y][x][0] == 0 and after[y][x][1] > 0 and after[y][x][1] == after[y][x][2]:
            # 나보다 생명이 클 때
            if after[y][x][1] > data[i][j][1]:
                pass
            # 나보다 생명이 작을 때
            else:
                after[y][x] = [0, data[i][j][1], data[i][j][1]]
    return after



def get_after(n, m, k, data):
    after = [[[0, 0, 0]] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            cell = data[i][j]
            # 죽은 세포
            if data[i][j][0] == -1:
                after[i][j] = data[i][j]
            # 비활성 세포
            elif data[i][j][0] == 0 and cell[1] > 0:
                # 비활성세포 대기시간이 끝남
                if data[i][j][2] == 0:
                    after[i][j] = [1, data[i][j][1], data[i][j][1]]
                # 비활성세포 대기시간 남음
                elif data[i][j][2] > 0:
                    after[i][j] = cell
            # 활성세포
            elif cell[0] == 1:
                # 대기시간 끝
                if cell[2] == 0:
                    after[i][j] = [-1, 0, 0]
                # 대기시간이 증식시간 끝난 경
                elif 0 < cell[2] < cell[1]-1:
                    after[i][j] == cell
                # 활성 후 첫 1시간
                elif cell[2] + 1 == cell[1]:
                    after = prolifer(i, j, n, m, k, data, after)
    return after



def sol(n, m, k, data):
    time_passed = 0
    # [is_active, life, left_hours] setting
    cells = set_data(n, m, k, data)
    n += 2*k
    m += 2*k
    while time_passed < k:
        # 1시간 지나면
        time_passed += 1
        before = hour_passed(n, m, k, cells)
        after = get_after(n, m, k, before)
        cells = after

    return count_alive(n, m, after)


T = int(input())
for tc in range(T):
    n, m, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    print(sol(n, m, k, data))
