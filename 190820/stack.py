s = []

def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        return
    else:
        return s.pop(-1)

def peek():
    if len(s) == 0:
        return
    else:
        return print(s[-1])


#sol
def push(item):
    stack[top] = item
    top 


push(9)
print(s)
push(8)
print(s)
push(7)
print(s)
pop()
print(s)
peek()
print(s)
pop()
print(s)
pop()
print(s)