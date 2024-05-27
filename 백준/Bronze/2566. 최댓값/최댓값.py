table = [list(map(int, input().split())) for _ in range(9)]

max_num = -float('inf')
max_row, max_col = 0, 0

for i in range(9):
    for j in range(9):
        if table[i][j] > max_num:
            max_num = table[i][j]
            max_row, max_col = i, j

print(max_num)
print(max_row + 1, max_col + 1)