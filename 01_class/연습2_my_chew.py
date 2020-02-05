# def isFull():
#     if front == rear and rear == len(q)-1:
#         return True
#     else:
#         return False
#
# def isEmpty():
#     if front == rear:
#         return True
#     else:
#         return False

def enQueue(i):
    q.append(i)

def deQueue():
    return q.pop(0)

candies = [0 for _ in range(20)]
visited = [0] * 20
total_candy = 20
q = []
front = -1
rear = -1

people_no = 1
enQueue(people_no)

while total_candy > 0:
    curr = deQueue()
    visited[curr] += 1
    if total_candy > visited[curr]:
        total_candy -= visited[curr]
        candies[curr] += visited[curr]
    else:
        total_candy -= total_candy
        candies[curr] += total_candy
        print("last candy goes to No.", curr)

    enQueue(curr)
    people_no += 1
    enQueue(people_no)
    print(q, candies[1:], total_candy)