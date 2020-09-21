# 2557
# print('Hello World!')

# 10718
# a = 1
# while a < 3:
#     print("강한친구 대한육군")
#     a += 1

# 10171
import sys

sys.stdin = open("1260_input.txt", "r")


data = [list(map(int, input().split())) for _ in range(m)]
dfs(data)
print()
bfs(data)
print()

