import sys
sys.stdin = open("2383_input.txt", "r")

"""
계단에는 동시에 3명까지만 올라갈 수 있다
    계단은 2개

조합으로 사람을 2 그룹으로 나눈다.

people_idx = [idx, dist]

각 조합에서 이동시간을 구하는데.....
    1. 계단에 도착하는 순서 구하기 => distance 구해서 sort
    
    도착하서 1분 기다리고 계단 이동 시작
    
    2. 모두가 이동을 완료할 시간 잡기
        2-1. if len(group) < 4: 제일 큰 distance + 계단 크기
        2-2. else: 
"""
import itertools


def find_stairs():
    result = []
    for i in range(n):
        for j in range(n):
            if data[i][j] > 1:
                result.append([i, j])
    return result


def find_people():
    result = []
    for i in range(n):
        for j in range(n):
            if data[i][j] == 1:
                result.append([i, j])
    return result


# 미리 각 구성원에 대한 두 계단 간의 거리를 측정해서 리스트에 넣어 놓으면 그 값만 가져오면 되니까 빠르겠지
# 근데 이 때 계단 길이 까지 더해서 (대기시간도) 미리 저장해 놓으면 좋겠지
# 큐나 리스트 지저분하게 쓸 것도 없이 그냥 하나의 리스트에 이동거리 넣어놓고 시간 += 1 할 때 마다 거리 -= 1 씩 해주고
# 완료 사람, 미완료 사람 따로 카운팅 해주면 간단하지

def get_distance(stair, people):
    return abs(stair[0] - people[0]) + abs(stair[1] - people[1])



def find(stair, comb):
    global max_time
    stair_depth = data[stair[0]][stair[1]]
    if comb:
        idx_dist = [[0] * 2 for _ in range(len(comb))]
        for i in range(len(comb)):
            idx_dist[i][0] = comb[i]
            idx_dist[i][1] = get_distance(stair, people[comb[i]])
        sorted_idx_dist = sorted(idx_dist, key=lambda x:x[1])

        if len(comb) < 4:
            time = sorted_idx_dist[-1][1] + 1 + stair_depth
        else:
            stair_q = []
            time = 0
            while sorted_idx_dist:
                time += 1
                for q in range(len(stair_q)):
                    stair_q[q][1] -= 1

                while stair_q:
                    if stair_q[0][1] == 0:
                        stair_q.pop(0)
                    else:
                        break

                for s in range(len(sorted_idx_dist)):
                    sorted_idx_dist[s][1] -= 1
                while len(stair_q) < 3 and sorted_idx_dist:
                    if sorted_idx_dist[0][1] < 0:
                        stair_q.append([sorted_idx_dist.pop(0)[0], stair_depth])
                    else:
                        break
            if stair_q:
                time += stair_q[-1][1]

        if max_time < time:
            max_time = time


T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    result = 10000

    stairs = find_stairs()
    people = find_people()
    total_people = len(people)

    people_idx = list(range(total_people))

    for r in range(total_people):
        combis = itertools.combinations(people_idx, r)
        for combi in list(combis):
            rest = list(set(list(range(total_people))) - set(list(combi)))

            max_time = 0
            find(stairs[0], list(combi))
            find(stairs[1], rest)
            if result > max_time:
                result = max_time

            max_time = 0
            find(stairs[1], list(combi))
            find(stairs[0], rest)
            if result > max_time:
                result = max_time

    print("#{} {}".format(tc+1, result))

# def comb():
#     if r == 0:
#
#     elif k > r:
#         return
#     else:
#         people[k] = arr[??]
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     data = [list(map(int, input().split())) for _ in range(n)]
#     result = 10000
#
#     stairs = find_stairs()
#     people = find_people()
#     total_people = len(people)
#
#     for r in range(total_people):
#         comb(r)
#
#     print("#{} {}".format(tc+1, result))