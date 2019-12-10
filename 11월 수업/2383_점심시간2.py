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
        

# 미리 각 구성원에 대한 두 계단 간의 거리를 측정해서 리스트에 넣어 놓으면 그 값만 가져오면 되니까 빠르겠지
# 근데 이 때 계단 길이 까지 더해서 (대기시간도) 미리 저장해 놓으면 좋겠지
# 큐나 리스트 지저분하게 쓸 것도 없이 그냥 하나의 리스트에 이동거리 넣어놓고 시간 += 1 할 때 마다 거리 -= 1 씩 해주고
# 완료 사람, 미완료 사람 따로 카운팅 해주면 간단하지
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


def get_distance(stairs, people):
    arr = [[0]*2 for _ in range(len(people))]
    for p in range(len(people)):
        for s in range(2):
            arr[p][s] = abs(stairs[s][0] - people[p][0]) + abs(stairs[s][1] - people[p][1])
    return arr


def find(comb, no):
    global max_time, first_depth, second_depth
    if no == 0:
        stair_depth = first_depth
    if no == 1:
        stair_depth = second_depth

    l = len(comb)
    waiting = [0] * l
    for i in range(l):
        waiting[i] = distances[comb[i]][no]
    sorted_waiting = sorted(waiting)
    time = 0
    if 0 < l < 4:
        time = sorted_waiting[-1] + 1 + stair_depth
    else:
        stair_q = [0] * len(comb)
        q_idx = 0
        q_cnt = 0
        while sorted_waiting:
            time += 1
            for q in range(q_idx):
                if stair_q[q] > 0:
                    stair_q[q] -= 1
                    if stair_q[q] == 0:
                        q_cnt -= 1
            for s in range(len(sorted_waiting)):
                sorted_waiting[s] -= 1
            while q_cnt < 3 and sorted_waiting and sorted_waiting[0] < 0:
                sorted_waiting.pop(0)
                q_cnt += 1
                stair_q[q_idx] = stair_depth
                q_idx += 1
        if q_cnt:
            time += max(stair_q)
    if max_time < time:
        max_time = time

T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    result = 10000
    stairs = find_stairs()
    first_depth = data[stairs[0][0]][stairs[0][1]]
    second_depth = data[stairs[1][0]][stairs[1][1]]
    people = find_people()
    total_people = len(people)
    distances = get_distance(stairs, people)
    people_idx = list(range(total_people))
    for r in range(total_people + 1):
        combis = list(itertools.combinations(people_idx, r))
        for combi in combis:
            rests = [rest for rest in people_idx if rest not in combi]
            max_time = 0
            find(list(combi), 0)
            find(rests, 1)
            if result > max_time:
                result = max_time
    print("#{} {}".format(tc + 1, result))

# visited 를 이용한 조합을 사용해도 ok