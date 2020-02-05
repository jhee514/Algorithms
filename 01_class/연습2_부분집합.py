nums = {n for n in range(1, 11)}

# sum이 10 이 되는 부분집합 구하기
# 가지치기는 다 더하기 전에 합이 10 이상이 되는 애들 제외

maxcandidates = len(nums)
nmax = len(nums)
a = [0] * nmax


def process_solution(a, k):
    total = 0
    for i in range(k):
        total += i
    if total == 10:
        return a[:k]

def contruct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(nums, k, input):
    global maxcandidates
    c = [0] * maxcandidates

    if k == input:
        process_solution(a, k)

    else:
        k += 1
        ncandidates = contruct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

for k in range(len(nums)):
    backtrack(nums, k, ?)