import sys
sys.stdin = open("input_5201.txt", "r")

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    container_raw = list(map(int, input().split()))
    truck_raw = list(map(int, input().split()))

    container = sorted(container_raw, reverse=True)
    truck = sorted(truck_raw, reverse=True)
    if n > m:
        cnt = m
    if n <= m:
        cnt = n
    c = -1
    total = 0
    used = [0] * m
    while cnt:
        c += 1
        if c == n:
            break
        for t in range(m):
            if truck[t] >= container[c] and not used[t]:
                total += container[c]
                used[t] = 1
                cnt -= 1
                break
    print("#{} {}".format(tc+1, total))