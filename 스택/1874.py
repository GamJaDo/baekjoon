import queue

make = True

stack = queue.LifoQueue()
result = []
cnt = 1

n = int(input())

for i in range(n):
    t = int(input())

    while cnt <= t:
        stack.put(cnt)
        result.append('+')
        cnt += 1
        
    if stack.get() == t:
        result.append('-')
    else:
        make = False
        print("NO")
        break

if make:
    for i in result:
        print(i)
