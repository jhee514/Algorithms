import sys
sys.stdin = open("input_4874.txt", "r")


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
    op = ['*', '+', '/', '-']
    for i in postfix:
        if i == '.':
            if len(s) ==1:
                return s.pop(-1)
            else:
                return 'error'
        if i in op:
            if len(s) > 1:
                if i == '*':
                    s.append(mult(s.pop(-2), s.pop(-1)))
                if i == '+':
                    s.append(add(s.pop(-2), s.pop(-1)))
                if i == '/':
                    s.append(div(s.pop(-2), s.pop(-1)))
                if i == '-':
                    s.append(sub(s.pop(-2), s.pop(-1)))
            else:
                return 'error'
        else:
            s.append(int(i))

T = int(input())
for t in range(T):
    data = list(input().split())
    print("#{} {}".format(t+1, calc_postfix(data)))