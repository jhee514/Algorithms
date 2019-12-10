import sys

sys.stdin = open("input_15683.txt", "r")
"""
1~5 번 카메라의 위치가 주어지면 각각의 함수에서 데이터를 처리하는데
할 때마다 데이터를 하나 카피한 판을 짜서
각 카메라가 커버되는 곳의 데이터를 # 으로 바꿔주고
카운팅하는 함수 따로 만들어서 사각지대를 계산하고 최솟값 찾기

방향의 조합
=> 1번의 경우 4방향, 2번은 2방향, 3번은 4방향, 4번도 4방향, 5번은 1방향
=> 2번도 편의를 위해 4방향이라 하고, 동서, 남북 방향을 같은 코드를 공유하게끔

카메라 찾는 함수 => 카메라 정보를 cam = [[no, i, j]...] 형태로 저장
각각 몇번 몇번 카메라가 있는지 저장
cam = [1, 2, 3, 4, 5]

5번 카메라 있으면 일단 #을 깔고 시작
# 으로 바꿀 때,
동서남북방향으로 커버치는 함수를 다 따로 만들어서(좌표를 변수로)
각각의 번호 함수에서 부를 수 있도록
후에 데이터 pan으로 복사 떠

min_zero = n*m
comb()
해서 dir = [             ] 조합 뽑아
dir 에 다 0~3까지 숫자를 중복조합으로 짜 넣어서

cover() 함수로 
 커버 되는 지역을 #으로 바꾸고

끝에서 0의 개수 카운팅
최솟값이면 result 를 업데이트

"""

import copy


def find_cams(data):
    no = list(range(1, 5))
    cam_list = []
    for i in range(n):
        for j in range(m):
            if data[i][j] in no:
                cam_list.append([data[i][j], [i, j]])
    return cam_list


def find_five(data):
    cam_list = []
    for i in range(n):
        for j in range(m):
            if data[i][j] == 5:
                cam_list.append([i, j])
    return cam_list


def north(point, arr):  # [a, b]
    a, b = point[0], point[1]
    for i in range(a - 1, -1, -1):
        if arr[i][b] == 6:
            return
        elif arr[i][b]:
            continue
        else:
            arr[i][b] = '#'


def south(point, arr):
    a, b = point[0], point[1]
    for i in range(a + 1, n):
        if arr[i][b] == 6:
            break
        elif arr[i][b]:
            continue
        else:
            arr[i][b] = '#'


def east(point, arr):
    a, b = point[0], point[1]
    for j in range(b - 1, -1, -1):
        if arr[a][j] == 6:
            break
        elif arr[a][j]:
            continue
        else:
            arr[a][j] = '#'


def west(point, arr):
    a, b = point[0], point[1]
    for j in range(b + 1, m):
        if arr[a][j] == 6:
            break
        elif arr[a][j]:
            continue
        else:
            arr[a][j] = '#'


def one(dir, point, arr):
    if dir == 0:
        north(point, arr)
    elif dir == 1:
        east(point, arr)
    elif dir == 2:
        south(point, arr)
    else:
        west(point, arr)


def two(dir, point, arr):
    if dir == 0 or dir == 2:
        north(point, arr)
        south(point, arr)
    else:
        east(point, arr)
        west(point, arr)


def three(dir, point, arr):
    if dir == 0:
        north(point, arr)
        east(point, arr)
    elif dir == 1:
        east(point, arr)
        south(point, arr)
    elif dir == 2:
        south(point, arr)
        west(point, arr)
    elif dir == 3:
        west(point, arr)
        north(point, arr)


def four(dir, point, arr):
    if dir == 0:
        west(point, arr)
        north(point, arr)
        east(point, arr)
    elif dir == 1:
        north(point, arr)
        east(point, arr)
        south(point, arr)
    elif dir == 2:
        east(point, arr)
        south(point, arr)
        west(point, arr)
    elif dir == 3:
        south(point, arr)
        west(point, arr)
        north(point, arr)


def five(point, data):
    north(point, data)
    south(point, data)
    east(point, data)
    west(point, data)


def count_zero(data):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                cnt += 1
    return cnt


def comb_dir(k, l):
    global min_cnt
    if k == l:
        pan = copy.deepcopy(data)
        for kk in range(l):
            if cam[kk][0] == 1:
                one(dir[kk], cam[kk][1], pan)
            elif cam[kk][0] == 2:
                two(dir[kk], cam[kk][1], pan)
            elif cam[kk][0] == 3:
                three(dir[kk], cam[kk][1], pan)
            elif cam[kk][0] == 4:
                four(dir[kk], cam[kk][1], pan)
        zero_cnt = count_zero(pan)
        if zero_cnt < min_cnt:
            min_cnt = zero_cnt
    else:
        for i in range(4):
            dir[k] = i
            comb_dir(k + 1, l)


for _ in range(6):
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
cam_five = find_five(data)
for f in cam_five:
    five(f, data)
cam = find_cams(data)
dir = [5] * len(cam)
min_cnt = n * m
comb_dir(0, len(cam))
print(min_cnt)
