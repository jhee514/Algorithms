def backtrack(k, sum):
    global cnt
    cnt += 1
    if k == N:
        if sum == 10:
            for i in range(1, 11):
                if a[i] == True:  # a 라는 배열 : 들어가나 안가나 1, 0 으로 처리
                    print(i, end=' ')
            print()
    else:
        k += 1
        if sum + k <= 10:
            a[k] = 1;
            backtrack(k, sum + k)

        a[k] = 1;
        backtrack(k, sum + k)
        a[k] = 0;
        backtrack(k, sum)

N = 10
a = [0] * (N + 1)

cnt = 0
backtrack(0, 0)
print("cnt : ", cnt)