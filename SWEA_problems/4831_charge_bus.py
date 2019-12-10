import sys
sys.stdin = open("input_bus.txt", "r")

def charge(k, n, m, chargers):
    bus = 0
    count = 0
    for i in range(m-1):
        if chargers[i+1] - chargers[i] > k:
            return 0
    else:
        while n - bus > k:
            for charger in chargers[::-1]:
                if charger - bus <= k:
                    count += 1
                    bus = charger
                    break
        return count

T = int(input())
for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    chargers = list(map(int, input().split()))
    print("#%d %d" % (tc, charge(k, n, m, chargers)))


# sol.
# for tc in range(1, T):
#     K, N, M = map(int, input().split())
#     stops = [0] + list(map(int, input().split())) + [N]
#
#     last = 0
#     cnt = 0
#     next = last + K
#
#     for i in range(1, M+2):
#         if (stop[i]-stop[i-1]) > K:
#             cnt = 0
#             break
#         if stops[i] > next:
#             last = stops[i-1]
#             cnt + =1
#
#         next  = last + K
#
#     print("#%d %d" % (tc, cnt))
