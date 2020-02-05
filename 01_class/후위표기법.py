text = "3+(4+5)*6+7"

def convert_postfix(string):
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
    return print(''.join(r))

convert_postfix(text)