import sys
sys.stdin = open("input_2231.txt", "r")

n = input()
num = int(n)
len_n = len(n)
m = num - 9 * len_n
ans = 0
while m < num:
    m_list = list(str(m))
    result = m
    for i in m_list:
        result += int(i)
    if result == num:
        ans = m
        break
    m += 1
print(ans)



# n = int(input())
# m = n - 1
# ans = 0
# while m > n * (0.1):
#     m_list = list(str(m))
#     result = m
#     for i in range(len(m_list)):
#         result += int(m_list[i])
#     if result == n:
#         ans = m
#     m -= 1
# if m > 0:
#     print(ans)
# else:
#     print('0')