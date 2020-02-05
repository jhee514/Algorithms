data = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
data_list = list(map(int, data.split()))
links = []
for i in range(len(data_list)//2):
    links.append(data_list[i*2:i*2+2])
n = 7

# def bfs_1(links):
#     q= []
#     v = [0] * 7
#     curr = 1
#     q.append(curr)
#     while q:
#         curr = q.pop(0)
#         print(curr, end=' ')
#         v[curr-1] = 1
#         for i in range(len(links)):
#             if links[i][0] == curr and not v[links[i][1]-1]:
#                 q.append(links[i][1])
#                 v[links[i][1]-1] = 1
#
#             if links[i][1] == curr and not v[links[i][0]-1]:
#                 q.append(links[i][0])
#                 v[links[i][0]-1] = 1
# print(bfs_1(links))
###########################################################

def isFull():
    global rear
    return rear == len(q) - 1

def isEmpty():
    return front == rear

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

def bfs_2(links):
    q = [0] * n
    v = [0] * n

    front = -1
    rear = -1

    enQueue(1)
    while not isEmpty():
        curr = deQueue()
        v[curr - 1] = 1
        for i in range(len(links)):
            if links[i][0] == curr and not v[links[i][1]-1]:
                enQueue(links[i][1])
                v[links[i][1]-1] = 1

            if links[i][1] == curr and not v[links[i][0]-1]:
                enQueue(links[i][0])
                v[links[i][0]-1] = 1
    return q

print(bfs_2(links))

############################################################

