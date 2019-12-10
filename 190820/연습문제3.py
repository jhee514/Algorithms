input_nums = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
nums = [input_nums[i*2 : i*2+2] for i in range(len(input_nums)//2)]

arr = [[0 for _ in range(8)] for _ in range(8)]

for num in nums:
    a, b = num[0], num[1]
    arr[a][b] += 1
    arr[b][a] += 1

stack = []
visited = []


n = 1
visited.append(n)
while len(visited) < 7:
    # w = n
    stack.append(n)
    for m in range(8):
        if arr[n][m]:
            if m == stack[-1]:
                pass
            if m not in visited:
                visited.append(m)
                n = m
                break

            if m in visited:
                # 갈림길이 나오는 번호 직전 까지 pop
                while sum(arr[stack[-1]]) < 3:
                    stack.pop(-1)
                else:
                    n = stack[-1]
                    stack.pop(-1)
                    # 여기서부터 m은 visited 에 없는 얘로 해야 range(stack[stack.index(n) + 1], 8)

print(visited)