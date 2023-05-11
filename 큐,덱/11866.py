import queue

n, k = map(int, input().split())

q = queue.Queue()

for i in range(n):
    q.put(i+1)

print("<", end = '')
while q.qsize():
    for _ in range(k-1):
        q.put(q.get())
    print(q.get(), end = '')

    if q.qsize() != 0:
        print(",", end = ' ')
print(">")
