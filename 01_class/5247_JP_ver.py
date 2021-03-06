import sys
sys.stdin = open('input.txt', 'r')
​
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    flag = False
    count = 0
    q = [N]
​
    while not flag:
        for _ in range(len(q)):
            cur = q.pop(0)
            if cur > M:
                result = [cur - 1, cur - 10]
            else:
                result = [cur + 1, cur - 1, cur * 2, cur - 10]
            for res in result:
                if res == M:
                    flag = True
                    break
                elif 0 < res < 1000000 and visited[res] == 0:
                    visited[res] = 1
                    q.append(res)
​
            if flag:
                break
        count += 1
​
    print('#{} {}'.format(t, count))