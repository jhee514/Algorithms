def solution(data):
    ans = ''

    n = len(data)
    each_length = [0] * n
    for i in range(n):
        each_length[i] = len(data[i])
    shortest_length = min(each_length)

    for j in range(shortest_length):
        for d in range(1, n):
            if data[0][j] != data[d][j]:
                return ans
        else:
            ans += data[0][j]
    return ans

data = ["abcdefg", "a"]
print(solution(data))