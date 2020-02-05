import sys
sys.stdin = open("input_4865.txt", "r")

T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    mxcnt = 0
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt += 1
        if cnt > mxcnt:
            mxcnt = cnt

    print("#%d %d" % (tc+1, mxcnt))

# sol.
# dictionary 사용해서 각각의 알파벳을 카운팅
# count = {}.fromkeys(str1, 0)
