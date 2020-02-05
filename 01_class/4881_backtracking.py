import sys
sys.stdin = open("input_4881.txt", "r")


def backtrack(a, k, input):
    global maxcandidates
    c= [0] * maxcandidates

    if k == input:
        print(a)
    else:
        k+=1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2


T = int(input())
for t in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    nmax = n
    maxcandidates = n
    a = [0] * nmax
    print(n, data)
    print(backtrack(a, 0, n))
    # print("#{} {}".format(t+1, find()))