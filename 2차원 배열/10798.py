arr = []
result = [[0 for _ in range(15)] for _ in range(5)]

for i in range(5):
    arr = list(input())

    for j in range(len(arr)):
        result[i][j] = arr[j]

for i in range(15):
    for j in range(5):
        if result[j][i] != 0:
            print(result[j][i], end = '')
