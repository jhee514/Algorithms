import sys
sys.stdin = open("input_4861.txt", "r")

def find(text, n, m):
    for i in range(n):
        for j in range(n-m+1):
            p = text[i][j:j+m]
            if p == p[::-1]:
                return ''.join(p)
    for l in range(n):
        for o in range(n-m+1):
            p = [text[q][l] for q in range(o, o+m)]
            if p == p[::-1]:
                return ''.join(p)

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    text = [list(input()) for _ in range(n)]
    print("#%d %s" % (tc+1, find(text, n, m)))


# sol.
# line 12 같이 계속 append를 해주게 되면 나중에 데이터가 커지면 시간이 많이 걸려서 비추
# TODO : 회문이니까 p의 절반만 가지고 M 만큼씩 알파벳을 잘라서 양쪽 알파벳을 하나씩 비교를 하면서 틀리면 다음 j 로 넘어가게 도록 j += 1 해주는 방ㅇ법