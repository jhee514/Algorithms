import sys

sys.stdin = open("input_calc.txt", "r")


def convert_postfix(text):
    isp = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2}
    icp = {"(": 3, "+": 1, "-": 1, "*": 2, "/": 2}
    s = []
    r = []
    top = -1
    for i in text:
        if i == ")":
            while s[top] != "(":
                r.append(s.pop(-1))
                top -= 1
            s.pop(-1)
            top -= 1
        elif i in isp.keys():
            if s:
                while s and not isp.get(s[-1]) < icp.get(i):
                    r.append(s.pop(-1))
                    top -= 1
                s.append(i)
                top += 1
            else:
                s.append(i)
                top += 1
        else:
            r.append(i)
    for i in s:
        r.append(i)
    return r


def add(a, b):
    return int(a) + int(b)


def sub(a, b):
    return int(a) - int(b)


def mult(a, b):
    return int(a) * int(b)


def div(a, b):
    return int(a) // int(b)


def calc_postfix(postfix):
    s = []
    for i in postfix:
        if i == '*':
            s.append(mult(s.pop(-1), s.pop(-1)))
        elif i == '+':
            s.append(add(s.pop(-1), s.pop(-1)))
        elif i == '/':
            s.append(div(s.pop(-1), s.pop(-1)))
        elif i == '-':
            s.append(sub(s.pop(-1), s.pop(-1)))
        else:
            s.append(int(i))
    return s.pop(-1)


T = 10
for t in range(T):
    n = int(input())
    data = input()
    print("#%d %d" % (t + 1, calc_postfix(convert_postfix(data))))
