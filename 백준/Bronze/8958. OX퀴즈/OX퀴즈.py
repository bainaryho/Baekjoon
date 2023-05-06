n = int(input())

for _ in range(n):
    li = list(input())
    score = 0
    sum_score = 0
    for i in li:
        if i == "O":
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)