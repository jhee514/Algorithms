import sys
sys.stdin = open("1932_input.txt", "r")


"""
DP 란다...........
MEMOIZATION!!!
아래부터 계산을 해나가면서 각 요소가 가질 수 있는 최대 값을 저장 시켜 놓고 역으로 올라가는 것....ㅜㅜ
"""

def sol(n, data):
    memo = list([0]*(i+1) for i in range(n))

    # memo 제일 하단 채우기
    memo[-1] = data[-1]

    for ii in range(n-2, -1, -1):
        for jj in range(ii+1):
            if memo[ii+1][jj] > memo[ii+1][jj+1]:
                memo[ii][jj] = memo[ii+1][jj] + data[ii][jj]
            else:
                memo[ii][jj] = memo[ii+1][jj+1] + data[ii][jj]
    return memo[0][0]


# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]
# print(sol(n, data))


########################################################################################

#
# """
# tree
# 모든 수는 양수
# 내려가면서 cur ele 의 idx 의 idx, idx+1 수 중 큰 수를 선택해서 내려가면 되는것
# 바보야 이렇게 가면 밑에가서 어떤 수를 만나는지 모르잖아
# 그르니까 모든 수를 다 비교해봐야하는거 아냐!??!
# 결국 dfs야....
# stack에 넣을 때 s = [[ele, row_idx, temp_sum], ] 이렇게 저장해야 하나????
# if row_idx == n-1 일 때 temp_sum값을 비교해봐야
# """
#
#
def solution(n, data):
    biggest = 0

    s = [[0, 0, data[0][0], [data[0][0]]]]
    while s:
        cur = s.pop(-1)
        cur_i, cur_j, temp_sum, path = cur[0], cur[1], cur[2], cur[3]

        if cur_i == n-1:
            if temp_sum > biggest:
                biggest = temp_sum
        else:
            for i in range(2):
                nex_i, nex_j =  cur_i+1, cur_j+i
                nex_ele = data[nex_i][nex_j]
                s.append([nex_i, nex_j, temp_sum+nex_ele, path+[nex_ele]])
    return biggest


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

import time
start = time.time()
print(sol(n, data))


print("time :", time.time() - start)
sec = time.time()
print(solution(n, data))
print("time :", time.time() - sec)


########################################################################################

"""
bfs
자신의 row 전후에 있는 row 들에 있는 값들 가운데
자신의 인덱스(i) 값과 같은 값을 갖거나 1 큰 인덱스를 갖는 애들이 후보
but 후보가 될 수 있는 index 의 range 가 중요
    len(data[j]) == j
    
visited 처리를 3차원 배열로 [boolean, depth, sum]으로 가져가보자 

q 를 이용하여 도는데, 이 때 종료 시점은 depth 가 n-1 일 때이다 => 시작 depth 는 0이다
"""

"""
왜 이걸 bfs 라고 생각했는지는 모르겠다
하지만 이 문제는 dfs로 접근해야한다.
최단 경로를 찾는 것이 아니라 끝까지 가봐야 답을 비교할 수 있기 때문.
이 문제의 경우 동서남북 네방향이 아닌 해당 숫자의 바로 아래행의 같은 열 또는 +1 열로만 이동 가능하기 때문에
visited 처리를 따로 해주지 않아도 된다.
"""

"""
def in_range(i, j, k):
    if 0 <= i < k and 0 <= j < i + 1:
        return True
    else:
        return False


def sol(n, data):
    s = [[0, 0]]
    visited = [list([0, 0, 0] for _ in range(i+1)) for i in range(n)]
    visited[0][0] = [1, 0, data[0][0]]
    max_dist = 0
    dir = [[1, 0], [1, 1]]
    while s:
        cur = s.pop(-1)
        for d in dir:
            dy, dx = cur[0] + d[0], cur[1] + d[1]
            if in_range(dy, dx, n):
                s.append([dy, dx])
                visited[dy][dx] = [1, dy, visited[cur[0]][cur[1]][2] + data[dy][dx]]
                if visited[dy][dx][1] == n - 1 and visited[dy][dx][2] > max_dist:
                    max_dist = visited[dy][dx][2]
    return max_dist


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
print(sol(n, data))
"""
