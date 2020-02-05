import sys
sys.stdin = open("5656_input.txt", "r")
"""
벽돌은 맨위에 있는 것만 깨는데,
    깨진 벽돌에 (새겨진 숫자 - 1) 만큼 상하좌우 벽돌을 같이 제거
    같이 제거되는 벽돌도 똑같이 그 위에 새겨진 숫자 - 1 만큼 상하좌우 벽돌 제거

제거하고 위에 붕 뜨는 애들 밑으로 내려주는 함수 

남은 벽돌 카운팅해주는 함수
"""

"""
1. 어디부터 깨부셔야 최소로 벽돌이 남는지 알아야 하니까
    => w 의 인덱스를 N개의 중복 조합으로 뽑아서
        => 부수는 함수는 재귀로
    
"""
# def explode(y, x):
#     for i in range(data[x][y]):
#         if data[y+i][x] > 1:
#             explode(y+i, x)
#         else:
#             data[y + i][x] = 0
#         if data[y-i][x] > 1:
#             explode(y-i, x)
#         else:
#             data[y - i][x] = 0
#         if data[y][x+i] > 1:
#             explode(y, x+1)
#         else:
#             data[y][x + i] = 0
#         if data[y][x-i] > 1:
#             explode(y, x-i)
#         else:
#             data[y][x-i] = 0
import copy

def copy_map():
    map = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            map[i][j] = raw[i][j]
    return map


def find_y_idx(x, data):
    y = 0
    while y < h:
        if data[y][x]:
            return y
        else:
            y += 1
    return 0

def explode(y, x, data):
    q = [0] * w * h
    visited = [[0]*w for _ in range(h)]
    front, rear = -1, -1
    rear += 1
    q[rear] = [y, x]
    visited[y][x] = 1
    while front != rear:
        front += 1
        cur = q[front]
        how_far = data[cur[0]][cur[1]]
        data[cur[0]][cur[1]] = 0
        if how_far:
            for i in range(how_far):
                dir = [(-i, 0), (i, 0), (0, -i), (0, i)]
                for d in dir:
                    yy, xx = cur[0] + d[0], cur[1] + d[1]
                    if 0<=yy<h and 0<=xx<w and not visited[yy][xx]:
                        visited[yy][xx] = 1
                        if data[yy][xx] > 1:
                            rear += 1
                            q[rear] = [yy, xx]
                        else:
                            data[yy][xx] = 0

# def explode(y, x, data):
#     q = [[y, x]]
#     while q:
#         cur = q.pop(0)
#         how_far = data[cur[0]][cur[1]]
#         data[cur[0]][cur[1]] = 0
#         if how_far:
#             for i in range(how_far):
#                 dir = [(-i, 0), (i, 0), (0, -i), (0, i)]
#                 for d in dir:
#                     yy, xx = cur[0] + d[0], cur[1] + d[1]
#                     if 0<=yy<h and 0<=xx<w:
#                         if data[yy][xx] > 1:
#                             q.append([yy, xx])
#                         else:
#                             data[yy][xx] = 0



def pick_x_idx(r=0):
    if r == n:
        map = copy_map()
        for x in x_idx:
            y = find_y_idx(x, map)
            explode(y, x, map)
            move(map)
        count_remain(map)
    else:
        for i in range(w):
            x_idx[r] = i
            pick_x_idx(r+1)


def move(data):
    for x in range(w):
        nums = [0] * h
        i = 0
        for y in range(h-1, -1, -1):
            if data[y][x]:
                nums[i] = data[y][x]
                i += 1
        for j in range(h):
            data[h-j-1][x] = nums[j]


def count_remain(data):
    global min_remains
    cnt = 0
    for i in range(h):
        for j in range(w):
            if data[i][j]:
                cnt +=1
    if cnt < min_remains:
        min_remains = cnt


T = int(input())
for tc in range(T):
    n, w, h = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(h)]

    min_remains = 9*w*h

    x_idx = [0] * n
    pick_x_idx()

    print("#{} {}".format(tc+1, min_remains))