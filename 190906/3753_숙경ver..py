T = int(input())
for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    results = [0]
    for i in scores:
        for j in range(len(results)):
            results.append(i + results[j])
        results = list(set(results))
    res = len(set(results))
    print('#%d %d' % (tc, res))