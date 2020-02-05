import sys
sys.stdin = open("input_17471.txt", "r")

"""
dfs 에서 같은 지역구 에 있는 ㅇㅐ들만 스택에 넣어야!!!
"""
"""
일단 두 선거구를 분리할 조합을 선정하고
    각 조합을 dfs로 모두 연결되어 있는지 체크 해주고 
        이게 된다면 각각의 선거구 인원을 체크해주고
            가장 최솟값을 찾아
"""


def dfs(comb):
    visited = [0] * (n+1)
    stack = [comb[0]]
    visited[comb[0]] = 1
    while stack:
        cur = stack.pop(-1)
        for j in range(1, n+1):
            if j in comb and cur != j and data[cur][j] and not visited[j]:
                stack.append(j)
                visited[j] = 1
    for c in comb:
        if not visited[c]:
            return False
    return True


def is_valid(comb):
    if dfs(comb):
        rest = []
        for i in range(1, n+1):
            if i not in comb:
                rest.append(i)
        if dfs(rest):
            return True

def comb(k, n, temp_pop = 0):
    global min_dif, flag
    if k == 0:
        if is_valid(temp_comb):
            flag = True
            if min_dif > abs(temp_pop - (total_pop - temp_pop)):
                min_dif = abs(temp_pop - (total_pop - temp_pop))
    elif n < k:
        return
    else:
        temp_comb[k-1] = no_vil[n-1]
        comb(k-1, n-1, temp_pop + pop_per_vil[temp_comb[k-1]])
        comb(k, n-1, temp_pop)


for _ in range(8):
    n = int(input())
    pop_per_vil = list(map(int, input().split()))
    pop_per_vil.insert(0, 0)
    data = [[0] * (n+1) for _ in range(n+1)]
    for vil in range(1, n+1):
        raw = list(map(int, input().split()))
        for t in range(1, raw[0] + 1):
            data[vil][raw[t]] = 1

    total_pop = sum(pop_per_vil)
    min_dif = total_pop
    no_vil = list(range(1, n+1))

    flag = False
    for k in range(1, n):
        temp_comb = [0] * k
        comb(k, n)

    if flag == False:
        print(-1)
    else:
        print(min_dif)