def comb(r, n):
    if r == 0:
        print(temp)
    elif n < r:
        return False
    else:
        temp[r-1] = nums[n-1]
        comb(r-1, n-1)
        comb(r, n-1)

num = 6
m = 3
nums = list(range(num))
temp = [0] * m
comb(m, num)

