from collections import deque

sorted = []
q = deque(sorted)


def enque(n):
    for j in range(len(q)):
        if n < q[j]:
            q.insert(j, n)
            break
    else:
        q.append(n)


def deque(q):
    return q.popleft()


enque(1)
print(q)
enque(5)
print(q)
enque(2)
print(q)
enque(4)
print(q)
enque(3)
print(q)

print(deque(q))
print(q)
print(deque(q))
print(q)
print(deque(q))
print(q)
print(deque(q))
print(q)
print(deque(q))
print(q)
