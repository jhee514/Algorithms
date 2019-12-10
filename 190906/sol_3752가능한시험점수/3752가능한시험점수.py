import sys

sys.stdin = open("input_3753.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    visited = [0]*(sum(scores)+1)
    visited[0]=1
    templist =[0]
    for elem in scores:
        for x in range(len(templist)):
            temp = templist[x]+elem
            if visited[temp] < 1:
                templist += [temp]
                visited[temp] = 1

    print("#%d %d" % (tc, sum(visited)))