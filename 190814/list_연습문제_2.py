arr = [1, 2, 3, -3, -2, 6, 5, -5, 8, 9]

subsets = []
for i in range(1 << len(arr)):
    subset = []
    for j in range(len(arr) + 1):
        if i & (1 << j):
            subset.append(arr[j])
    subsets.append(subset)
for subset in subsets:
    total = 0
    for s in subset:
        total += s
    if total == 0:
        print(subset)