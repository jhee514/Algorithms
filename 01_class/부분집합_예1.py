arr = [1, 5, -9, 6, -2]

subsets = []
for i in range(1 << len(arr)):
    subset = []
    for j in range(len(arr)+1):
        if i & (1 << j):
            subset.append(arr[j])
    subsets.append(subset)

print(subsets)