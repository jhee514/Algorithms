def route(cnt, prev, dist):
    global mindist

    if cnt == N+1:
        dist += D[prev][N+1]
        if dist < mindist:
            mindist = dist
            return

    for i in range(cnt, N+1):
        chk[i] , chk[cnt] = chk[cnt], chk[i]
        d = dist + D[prev][chk[cnt]]
        if d < mindist :
            route(cnt+1, chk[cnt], d)
        else:
            chk[i], chk[cnt] = chk[cnt], chk[i]
            break
        chk[i] , chk[cnt] = chk[cnt], chk[i]

for tc in range(int(input())):
    N = int(input())

    indata = list(map(int, input().split()))
    indata.append(indata.pop(2))
    indata.append(indata.pop(2))
    D = [[0]*(N+2) for _ in range(N+2)]
    for i in range(N+2):
        for j in range(i,N+2):
            D[i][j] = abs(indata[i*2] - indata[j*2])+abs(indata[i*2+1] - indata[j*2+1])
            D[j][i] = D[i][j]

    mindist = 2400
    chk = [i for i  in range(N+2)]
    route(1, 0, 0)
    print("#%d %d" % (tc+1, mindist))
