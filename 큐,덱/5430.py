import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    reverse = 0
    sw = 1
    ac = input()
    n = int(input())
    arr = deque(input().strip()[1:-1].split(','))

    if arr[0] == '':
        arr = deque()

    for i in ac:
        if i=='R':
            reverse += 1
            
        elif i == 'D':
            if len(arr) == 0:
                sw = 0
                print("error")
                break
            else:
                if reverse%2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    if sw:
        if reverse%2 == 0:
            print("[" + ",".join(arr) + "]")
        else:
            arr.reverse()
            print("[" + ",".join(arr) + "]")
