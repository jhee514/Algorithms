import sys
sys.stdin = open("input_sub.txt", "r")

def find(subsets):
    count = 0
    for sub in subsets:
        if len(sub) == n:
            total = sub[0]
            for i in range(1, len(sub)):
                total += sub[i]
            if total == k:
                count += 1
    return count

T = int(input())
arr = [num for num in range(1, 13)]
subsets = []
for i in range(1 << len(arr)):
    subset = []
    for j in range(len(arr)+1):
        if i & (1 << j):
            subset.append(arr[j])
    subsets.append(subset)

for t in range(T):
    n, k = map(int, input().split())

    print("#%d %d" % (t+1, find(subsets)))
