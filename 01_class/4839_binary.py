import sys
sys.stdin = open("input_binary.txt", "r")

def find(l, r, target, count):
    c = int((l + r)/2)
    count += 1
    if c == target:
        return count
    elif target > c:
        l = c
        return find(l, r, target, count)
    elif target < c:
        r = c
        return find(l, r, target, count)

T = int(input())
for t in range(T):
    p, a, b = map(int, input().split())
    if find(1, p, a, 0) > find(1, p, b, 0):
        result = 'B'
    elif find(1, p, a, 0) < find(1, p, b, 0):
        result = 'A'
    else:
        result = 0
    print("#%d %s" % (t+1, result))



# sol.
