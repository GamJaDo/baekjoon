page = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())
for _ in range(n):
    hight, width = map(int, input().split())

    for i in range(10):
        for j in range(10):
            page[hight+i][width+j] = 1

result = 0

for i in range(100):
    for j in range(100):
        result += page[i][j]

print(result)
