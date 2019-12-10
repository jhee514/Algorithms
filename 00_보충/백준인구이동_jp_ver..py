import sys
sys.stdin = open('input.txt', 'r')
​
import time
start_time = time.time()
​
def is_wall(arr, x, y):
    return x < 0 or y < 0 or x >= N or y >= N or arr[x][y]
​
def find_nation(world, nation, x, y, nation_num):
    q = [(x, y)]
    path = []
    sum = 0
    while q:
        x, y = q.pop(0)
        if nation[x][y] == 0:
            sum += world[x][y]
            path.append((x, y))
            nation[x][y] = nation_num
        else:
            continue
​
        for vector in directions:
            next_x, next_y = x + vector[0], y + vector[1]
            if is_wall(nation, next_x, next_y):
                continue
            else:
                gap = abs(world[x][y] - world[next_x][next_y])
                if L <= gap <= R:
                    q.append((next_x, next_y))
    return sum//len(path)
​
N, L, R = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
nation_num = 0
count = 0
​
while 1:
    nation = [[0] * N for _ in range(N)]
    nation_num = 0
    popular = {}
    for i in range(N):
        for j in range(N):
            if nation[i][j] == 0:
                nation_num += 1
                popular[nation_num] = find_nation(world, nation, i, j, nation_num)
​
    if nation_num == N*N:
        break
​
    for i in range(N):
        for j in range(N):
            world[i][j] = popular.get(nation[i][j])
    count += 1
​
print(count)
print(time.time() - start_time)