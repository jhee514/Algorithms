import sys
sys.stdin = open('16236_input.txt', 'r')
"""
1. 아가 위치 파
    아기상어 초기값 => 2
    baby_size = 2
    dinner_time = 0


2. 먹을 거리 개수 파악
    물고기 개수 파악 => 먹을 때마다 left_fish -= 1

if left_fish == 0:
    return dinner_time

else:
    3. 물고기 먹기
    while left_fish:
        3-1. 아가 위치 파악
            baby = find_baby()

        3-2. 먹을 수 있는 물고기 1개 => 먹어
        if left_fish == 1:
            fish = find_nearest_fish()
            dinner_time += abs(fish[0][0] - baby[0]) + abs(fish[0][1]) - baby[1)
            break

        3-3. 먹을 수 있는 물고기 많다면 가장 가까운 물고기 먼저 먹기
            거리 가장 가까운 물고기가 여럿이면 제일 위 + 제일 왼쪽 물고기 먹기
            1칸 / 1초
            1. 단, 자신보다 큰 물고기 있는 칸 이동 못해
            2. 자기보다 작은 물고기 먹어
            3. 크기가 같은 물고기는 먹지는 못하고 지나가기만

        while q:
            temp_q = []
            possible_dinner = []
            visited = [[0]*n for _ in range(n)]
            visited[cur[0]][cur[1]] = 1
            ...
            for dir in direction:
                if 0<=x<n and 0<=y<n and data[y][x]<= baby_size:
                    if data[y][x] == baby_size:
                        temp_q.append([y, x])
                    elif data[y][x] < baby_size:
                        possible_dinner.append([y, x])
                    visited[y][x] = visited[cur[0]][cur[1]] + 1

            if possible_dinner:
                if len(possible_dinner) == 1:
                    fish = possible_dinner[0]
                else:
                    fish = 거리 가장 가까운 물고기가 여럿이면 제일 위 + 제일 왼쪽 물고기 골라서
                dinner_time += visited[fish[0]][fish[1]] - 1
                left_fish -= 1
                data[y][x] = 9
                data[cur[0]][cur[1]] = 0

                고기 / 아가 크기계산
                if num_of_eaten_fish == baby_size;
                    baby_size += 1
                    num_of_eaten_fish = 0

                q = []
            else:
                q += temp_q
"""

def count_dinner(n, data):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if 0 < data[i][j] < 7:
                cnt += 1
    return cnt


def find_baby(n, data):
    for i in range(n):
        for j in range(n):
            if data[i][j] == 9:
                return [i, j]


def find_nearest_fish(n, data):
    for i in range(n):
        for j in range(n):
            if 0 < data[i][j] < 7:
                return [i, j]


def find_topnleft(fishes):
    sorted(fishes, key=lambda position: position[0])
    sorted(fishes, key=lambda position: position[1])
    return fishes[0]


def find(n, data):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    baby_size = 2
    dinner_time = 0
    eaten_fish = 0
    left_fish = count_dinner(n, data)

    if left_fish == 0:
        return dinner_time
    else:
        baby = find_baby(n, data)

        while left_fish:
            if left_fish == 1:
                fish = find_nearest_fish(n, data)
                dinner_time += abs(fish[0] - baby[0]) + abs(fish[1] - baby[1])
                return dinner_time
            else:
                visited = [[0] * n for _ in range(n)]
                q = [baby]
                visited[baby[0]][baby[1]] = 1
                while q:
                    temp_q = []
                    possible_dinner = []
                    cur = q.pop(0)
                    for dir in range(4):
                        y, x = cur[0] + directions[dir][0], cur[1] + directions[dir][1]
                        if 0 <= x < n and 0 <= y < n and data[y][x] <= baby_size and not visited[y][x]:
                            visited[y][x] = visited[cur[0]][cur[1]] + 1
                            if 0 < data[y][x] < baby_size:
                                possible_dinner.append([y, x])
                            else:
                                temp_q.append([y, x])
                    if possible_dinner:
                        fish = find_topnleft(possible_dinner)
                        baby = fish
                        data[cur[0]][cur[1]] = 0
                        data[fish[0]][fish[1]] = 9
                        dinner_time += visited[fish[0]][fish[1]] - 1
                        left_fish -= 1

                        eaten_fish += 1
                        if eaten_fish == baby_size:
                            baby_size += 1
                            eaten_fish = 0
                        q = []
                    else:
                        q += temp_q

        return dinner_time


for tc in range(6):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    print(find(n, data))