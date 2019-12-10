import sys
sys.stdin = open("input_5208.txt", "r")

#######################################
# JW ver.
# def bt(stop, cnt):
#     global mn
#     global Ms
#     if cnt >= mn:
#         return
#     new_battery = Ms[stop]
#     if stop + new_battery >= N - 1:
#         mn = min(mn, cnt)
#         return
#     for battery_usage in range(new_battery, -1, -1):
#         bt(stop + battery_usage, cnt +1)
#
# T = int(input())
# for tc in range(T):
#     data = list(map(int, input().split()))
#     N = data[0]
#     Ms = data[1:]
#     mn = N
#     bt(0, 0)
#     print(mn)

#######################################
# JP ver.
def find(battery, now_bat, change, cur):
    global min_value
    if cur == len(battery):
        if min_value > change:
            min_value = change
    else:
        if now_bat > 0:
            find(battery, now_bat -1, change, cur+1)
        if min_value > change:
            find(battery, battery[cur]-1, change+1, cur +1)
T = int(input())
for t in range(1, T+1):
    station = list(map(int, input().split()))
    N = station[0]
    battery = station[1:]
    min_value = 100000000

    find(battery, battery[0], 0, 0)
    print(min_value)