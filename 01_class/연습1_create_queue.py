def isFull():
    if front == rear and rear == len(q)-1:
        return True
    else:
        return False

def isEmpty():
    if front == rear:
        return True
    else:
        return False

def enQueue(i):
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear += 1
        q[rear] = i

def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front += 1
        return q[front]


n = 5
q = [0] * n
front = -1
rear = -1
data = [1, 2, 3]
for i in data:
    enQueue(i)
    print(front)
    print(q)

for i in range(4):
    a = deQueue()
    print("front", front)
    print(a)
print(q)



