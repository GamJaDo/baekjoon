#최소힙 이므로 최대힙을 구할려면-1을 곱한다
import sys
import heapq

input = sys.stdin.readline

heap = []

n = int(input())

for _ in range(n):
    t = int(input())
    
    if t == 0:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print("0")
    else:
        heapq.heappush(heap, -1*t)
