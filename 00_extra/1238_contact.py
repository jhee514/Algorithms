import sys

sys.stdin = open("input_1238.txt", 'r')


def find(contacts):
    arr = [[0] * 101 for _ in range(101)]
    for i in range(len(contacts)):
        arr[contacts[i][0]][contacts[i][1]] = 1

    q = []
    visited = [0] * 101

    curr = start
    q.append(curr)
    visited[curr] = 1

    while q:
        maxnum = max(q)
        mark = len(q)

        for j in range(mark):
            curr = q.pop(0)
            # visited[curr] = 1  => 꺼낼 때 표시를 해주면 아래 for 문 도는 사이에 중복된 요소를 append 해 줄 기회가 생겨버려
            for i in range(101):
                if arr[curr][i] and not visited[i]:
                    q.append(i)
                    visited[i] = 1
    return maxnum


T = 10
for tc in range(T):
    n, start = map(int, input().split())
    data = list(map(int, input().split()))
    contacts = [data[i * 2: i * 2 + 2] for i in range(len(data) // 2)]
    print("#%d %d" % (tc + 1, find(contacts)))
