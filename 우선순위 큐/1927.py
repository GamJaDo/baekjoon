import sys
import heapq

input = sys.stdin.readline

heap = []

n = int(input())

for _ in range(n):
    t = int(input())
    
    if t == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print("0")
    else:
        heapq.heappush(heap, t)
