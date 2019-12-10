def comb(data, n, r):
    global cnt
    if r == 0:
        if sum(temp) == 0:
            print(temp)
            cnt += 1
            return
    elif n < r:
        return
    else:
        temp[r-1] = data[n-1]
        comb(data, n-1, r-1)
        comb(data, n-1, r)

def binary_cnt(arr):
    count = 0
    for i in range(0, (1 << n)):  # i << n : 부분집합의 개수
        tt = []
        sum = 0
        for j in range(n):  # 원소의 수만큼 비트를 비교
            if i & (1 << j):  # i의 j 번째 비트가 1이면 j 번째 원소 출력
                tt.append(arr[j])
                sum += arr[j]  # 여기서 같이 연산을 하면 쁘르지
        if sum == 0:
            print(tt)
            count += 1
    print("bi :", count)

nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(nums)

cnt = 0
for i in range(n):
    temp = [0] * i
    comb(nums, n, i)
print("comb: ", cnt)

binary_cnt(nums)