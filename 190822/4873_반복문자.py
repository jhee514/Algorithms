import sys
sys.stdin = open("input_4873.txt", "r")


def isempty(list):
    if len(list) == 0:
        return 1
    else:
        return 0

def find(text):
    s = []
    for i in text:
        if isempty(s):
            s.append(i)
        elif not isempty(s) and s[-1] != i:
            s.append(i)
        elif not isempty(s) and s[-1] == i:
            s.pop(-1)
    return len(s)

T = int(input())
for tc in range(T):
    text = input()
    print("#%d %s" % (tc+1, find(text)))