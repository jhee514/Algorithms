import sys
sys.stdin = open("input_4866.txt", "r")


def find(text):
    pairs = {'{':'}', '(':')', '[':']'}
    st = []

    for t in text:
        if t in pairs.keys():
            st.append(t)

        if t in pairs.values():
            if len(st):
                for k, v in pairs.items():
                    if t == v:
                        if st[-1] == k:
                            st.pop(-1)
                        else:
                            return 0
            else:
                return 0

    if len(st) == 0:
        return 1
    else:
        return 0

T = int(input())
for tc in range(T):
    text = input()
    print("#%d %d" % (tc+1, find(text)))