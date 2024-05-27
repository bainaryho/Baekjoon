max_num = -1
max_row, max_col = 0, 0

for i in range(9):
    arr = list(map(int,input().split()))
    for j in range(9):
        if arr[j] > max_num:
            max_num = arr[j]
            max_row, max_col = i, j

print(max_num)
print(max_row+1, max_col+1)