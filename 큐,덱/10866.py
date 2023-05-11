import sys
from collections import deque

def Empty(q):
    return (len(q) == 0)

n = int(input())

q = deque([])

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        q.appendleft(command[1])
    elif command[0] == 'push_back':
        q.append(command[1])
    elif command[0] == 'pop_front':
        if not(Empty(q)):
            print(q.popleft())
        else:
            print("-1")
    elif command[0] == 'pop_back':
        if not(Empty(q)):
            print(q.pop())
        else:
            print("-1")
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if len(q):
            print("0")
        else:
            print("1")
    elif command[0] == 'front':
        if not(Empty(q)):
            print(q[0])
        else:
            print("-1")
    elif command[0] == 'back':
        if not(Empty(q)):
            print(q[-1])
        else:
            print("-1")
