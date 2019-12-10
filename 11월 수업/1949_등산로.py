import sys
sys.stdin = open("1949_input.txt", "r")

"""
1.가장 높은 봉우리에서 시작한다
    => 가장 높은 칸의 인덱스를 취합
2. 높은 데서 낮은 곳으로만! 사방으로만! 이동 가능
    => 각각의 시작점에 대해 depth-fs로 해서 visited 대신 depth 를 표시

    3. 딱 한칸만! 최대 k 만큼 지형을 깍는!! 공사 가능
        => 막히는 구간에서 한번 k 만큼 data 를 깎아서 들어가는데...
            => 이걸 표시를 어케 해주지!??!?!?
            
            => 이걸 COPY를 안 쓰고 구할 방법!!
                => constructed 로 값을 따로 들고가

"""

def in_square(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True
    else:
        return False


def find_start(data):
    max_points = []
    max_height = max(map(max, data))
    for i in range(n):
        for j in range(n):
            if data[i][j] == max_height:
                max_points.append([i, j])
    return [max_height, max_points]


def find_path(point, point_height, depth=1, contruction=1):
    global max_length
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    for dir in range(4):
        y, x = point[0] + directions[dir][0], point[1] + directions[dir][1]
        if in_square(y, x) and not visited[y][x]:
            if data[y][x] < point_height:
                visited[y][x] = 1
                find_path([y, x], data[y][x], depth+1, contruction)
                visited[y][x] = 0
            elif contruction > 0 and data[y][x] - point_height < k:
                for kk in range(data[y][x] - point_height + 1, k+1):
                    visited[y][x] = 1
                    find_path([y, x], data[y][x] - kk, depth+1, contruction - 1)
                    visited[y][x] = 0
            """
            elif contruction > 0 and data[y][x] - point_height < k:
                visited[y][x] = 1
                find_path([y, x], data[y][x] - 1, depth+1, contruction - 1)
                visited[y][x] = 0
            kk 로 for 문 돌지말고 무조건 '나' 보다 1 만 깎아주면 빨라진다.(by JP)
            """
        else:
            if max_length < depth:
                max_length = depth


T = int(input())
for tc in range(T):
    n, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    max_values = find_start(data)
    max_height, starting_points = max_values[0], max_values[1]
    max_length = 0
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    for point in starting_points:
        stack = [point]
        visited = [[0] * n for _ in range(n)]
        visited[point[0]][point[1]] = 1
        find_path(point, max_height)
    print("#{} {}".format(tc+1, max_length))



















#######################################################################
        # visited = [[0] * n for _ in range(n)]
        # q = [0] * (n*n)
        # front, rear = -1, -1
        #
        # front += 1
        # q[front] = point
        # while front != rear:
        #     rear += 1
        #     cur = q[rear]
        #     for dir in directions:
        #         y, x = cur[0]+dir[0], cur[1]+dir[1]
        #         if in_square(y, x) and data[y][x] < data[cur[0]][cur[1]]:



