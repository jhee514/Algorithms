import sys

sys.stdin = open("input_14501.txt", "r")


# 부분집합을 일단 다 만든 후에 해당 일자들이 겹치지 않는지 판단하고 => visitied
# 겹치지 않는 부분집합의 상담료를 더한 값을 구한 후, 그 중 max 를 판

# def construct_candidates(a, k, input, c):
#     c[0] = True
#     c[1] = False
#     return 2

def process_solution(a):
    day = [0] * n
    total = 0
    for i in range(n):
        if a[i] == True:
            for j in range(i, i + data[i][0]):
                if not day[j]:
                    day[j] = 1
                    total += data[i][1]
                else:
                    return False
    return total


#
# def backtrack(a, k, n):
#     c = [0] * 100
#     if k == n:
#         print(process_solution(a)) # 답이면 원하는 작업을 한다
#     else:
#         k += 1
#         ncandidates = construct_candidates(a, k, input, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k, input)

def backtrack(k, sum=0):
    if k == n:
        process_solution(a)
    else:
        k += 1
        for i in range(2):
            a[k] = i
            if a[k] == 1:
                sum += data[k - 1][0]
                backtrack(k, sum)
            elif a[k] == 0:
                backtrack(k, sum)


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
a = [0] * (n + 1)
backtrack(a, 0, n)
