"""
즉, NxN의 꿀통 판에서
M 개의 가로로 연속된 꿀통의 제곱합이 C 와 같거나 가장 가까운 집합을 M 개 뽑아 내는데,
이 때, 두 집합이 겹치면 안됑
여기서만 인덱싱이 중요하고
각 열마다 최대 제곱합의 값을 두개씩 뽑아서
뽑아낸 집합의 가장 큰 두개 합의 합을 출력
"""
"""
arr = [0]* n 이라는 빈 어레이 짜고
    여기다 각 스타트 포인트에 M 개의 합 값을 넣어
    그리고 다음열로 넘어갈 때 리셋
    
max_honey = [[0]*2 for _ in range(n)]
  
1. 가로마다 돌면서 합이 C 보다 같거나 작고 + 가장 제곱합이 가장 큰 조합을 두개씩 뽑아 낸다
    1-1.m개의 조합 합 구하기 
        for i in range(n):
            arr = [0]* n
            for j in range(0, n-1):
                if sum(data[i][j:j+m]) > C:
                    arr[j] = C**C
                else:
                    제곱의 합
    
    1-2. 합이 가장 크고 서로 겹치지 않는 2개 집합 골라내기
        arr => deepcopy
        copy_arr.sort(reverse=True)
        max_honey[i][0] = copy_arr[0]
        for j in range(1, n-1):
            if data[i].index(copy_arr[0]) + (m-1) < data.index(copy_arr[j]):
                max_honey[i][1]
                break
        
2. 큰 조합의 집합에서 겹치지 않는 M 개의 합이 큰 애들을 골라
    max_honey.sort()
    result = max_honey[0] + max_honey[1] 
"""
import sys
sys.stdin = open("input_2115.txt", "r")

# TODO comb 없이 코드 짜보기
import copy

def comb(r, m, honey = 0):
    global max_comb
    if r == 0:
        if honey > max_comb:
            max_comb = honey
            arr[j] = honey
            return True
    elif n < r:
        return
    else:
        comb(r-1, m-1, honey + a[m-1]*a[m-1])
        comb(r, m-1, honey)



T = int(input())
for tc in range(T):
    n, m, c = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    max_honey = [[0] * 2 for _ in range(n)]
    for i in range(n):
        arr = [0] * n
        for j in range(0, n - m+1):
            if sum(data[i][j:j + m]) > c:

                a = data[i][j:j + m]
                max_comb = 0
                for r in range(m, 0, -1):
                    if comb(r, m):
                        break


                arr[j] = max_comb
            else:
                arr[j] = sum([data[i][j+k]*data[i][j+k] for k in range(m)])
        sorted_arr = copy.deepcopy(arr)
        sorted_arr.sort(reverse=True)
        max_honey[i][0] = sorted_arr[0]
        for a in range(1, n):
            if arr.index(sorted_arr[0]) + (m - 1) < arr.index(sorted_arr[a]):
                max_honey[i][1] = sorted_arr[a]
                break
    result = 0
    for _ in range(2):
        max_temp = 0
        max_point = [0, 0]
        for ii in range(n):
            for jj in range(2):
                if max_honey[ii][jj] > max_temp:
                    max_temp = max_honey[ii][jj]
                    max_point = [ii, jj]
        result += max_honey[max_point[0]][max_point[1]]
        max_honey[max_point[0]][max_point[1]] = 0
    print("#{} {}".format(tc+1, result))



# import sys
# sys.stdin = open("input_2115.txt", "r")
#
#
# import copy
#
# def comb(r, n, a):
#     global max_comb
#     if r == 0:
#         if sum(temp) <= c:
#             if max_comb < sum([t*t for t in temp]):
#                 max_comb = sum([t*t for t in temp])
#                 return True
#     elif n < r:
#         return
#     else:
#         temp[r-1] = a[n-1]
#         comb(r-1, n-1, a)
#         comb(r, n-1, a)
#
#
#
# T = int(input())
# for tc in range(T):
#     n, m, c = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(n)]
#     max_honey = [[0] * 2 for _ in range(n)]
#     for i in range(n):
#         arr = [0] * n
#         for j in range(0, n - m+1):
#             if sum(data[i][j:j + m]) > c:
#                 a = data[i][j:j + m]
#                 max_comb = 0
#                 for r in range(m, 0, -1):
#                     temp = [0] * r
#                     if comb(r, m, a):
#                         break
#                 arr[j] = max_comb
#             else:
#                 arr[j] = sum([data[i][j+k]*data[i][j+k] for k in range(m)])
#         sorted_arr = copy.deepcopy(arr)
#         sorted_arr.sort(reverse=True)
#         max_honey[i][0] = sorted_arr[0]
#         for a in range(1, n):
#             if arr.index(sorted_arr[0]) + (m - 1) < arr.index(sorted_arr[a]):
#                 max_honey[i][1] = sorted_arr[a]
#                 break
#     result = 0
#     for _ in range(2):
#         max_temp = 0
#         max_point = [0, 0]
#         for ii in range(n):
#             for jj in range(2):
#                 if max_honey[ii][jj] > max_temp:
#                     max_temp = max_honey[ii][jj]
#                     max_point = [ii, jj]
#         result += max_honey[max_point[0]][max_point[1]]
#         max_honey[max_point[0]][max_point[1]] = 0
#     print("#{} {}".format(tc+1, result))
