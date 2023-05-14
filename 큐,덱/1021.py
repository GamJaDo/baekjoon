from collections import deque

n, m = map(int, input().split())

q = deque()
for i in range(1, n+1):
    q.append(i)

out = list(map(int, input().split()))
cnt = 0

for i in out:
    if len(q)//2 < q.index(i):
        t = q.pop()
        
        while t != i:
            q.appendleft(t)
            cnt += 1
            t = q.pop()
            
        q.appendleft(t)
        cnt += 1
        q.popleft()
    else:
        t = q.popleft()

        while t != i:
            q.append(t)
            cnt += 1
            t = q.popleft()

        q.appendleft(t)
        q.popleft()
print(cnt)
