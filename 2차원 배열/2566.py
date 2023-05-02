board = []
max_value = -1
index_i = 0
index_j = 0

for _ in range(9):
    board.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if board[i][j] > max_value:
            max_value = board[i][j]
            index_i = i
            index_j = j

print(max_value)
print(index_i+1, index_j+1)
