s = []

def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        return
    else:
        return s.pop(-1)

def find(test):
    left = ['[', '(', '{']
    for i in test:
        if i in left:
            push(i)
        else:
            if len(s):
                pop()

    if len(s) == 0:
        return 1
    else:
        return  0

t1 = '()()((()))'
t2 = '((()((((()()((()())((())))))'

print(find(t1), find(t2))