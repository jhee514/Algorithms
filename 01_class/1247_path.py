import sys

sys.stdin = open("input_1247.txt", "r")
# sys.stdout = open("output_1247_perm.txt", "w")

import time

start = time.time()


def calc_dist(l):
    global minD
    result = 0
    for i in range(len(l) - 1):
        result += abs(data[l[i]][0] - data[l[i + 1]][0]) + abs(data[l[i]][1] - data[l[i + 1]][1])
    if result < minD:
        minD = result
    return


def perm(k, N):
    global minD
    if k == N:
        result = [0] * (N + 2)
        result[0] = 0
        result[N + 1] = 1
        total = 0
        for i in range(0, N):  # arr[i] 가 index
            result[i + 1] = arr[i]
        calc_dist(result)

    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k + 1, N)
            arr[k], arr[i] = arr[i], arr[k]

T = int(input())
for tc in range(T):
    n = int(input())
    raw_data = list(map(int, input().split()))
    data = [0] * (n + 2)  # => data : 좌표 리스트의 리스트
    for i in range(n + 2):
        data[i] = raw_data[i * 2: (i + 1) * 2]

    arr = [j for j in range(2, n + 2)]
    minD = 1000000
    perm(0, n)

    print("#{} {}".format(tc + 1, minD))
    print("time :", time.time() - start)
print("time :", time.time() - start)

##########################################################################################

# T = int(input())
# for tc in range(T):
#     n = int(input())
#     raw_data = list(map(int, input().split()))
#     data = [0] * (n+2)  # => data : 좌표 리스트의 리스트
#     for i in range(n+2):
#         data[i] = raw_data[i * 2: (i + 1) * 2]
#
#     # data = 고객 위치
#     # data 의 개수 만큼의 인덱스 리스트를 생성해서 이걸 순열로 만들어내
#     # 각각의 순열을 모두 점검
#     # 회사 - 고객1 - 고객2 - ... - 집 거리를 구해서 다 더한 값을 도출
#     # 회사에서 첫 고객 까지 거리 우선 total 에 더하고
#     # 고객간 거리
#     # 마지막 고객에서 집까지 거리
#     # 가장 짧은 값 내기
#
#     arr = [j for j in range(2, n+2)]
#     perm(0, n)
#
#     # orders = list(permutations(data))
#     min_dist = 1000000
#     # for order in orders:
#     #     total = 0
#     #     total += calc_dist(company, order[0])
#     #     for j in range(len(order) - 1):
#     #         total += calc_dist(order[j], order[j + 1])
#     #     total += calc_dist(order[-1], home)
#     #     if total < min_dist:
#     #         min_dist = total
#
#     print("#{} {}".format(tc + 1, min_dist))
#
# print("time :", time.time() - start)