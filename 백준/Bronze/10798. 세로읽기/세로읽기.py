# 입력을 받는 부분
words = [input() for i in range(5)]

# 최대 길이를 계산하는 부분
max_length = max(len(word) for word in words)

# 처리하는 부분
for j in range(max_length):
    for i in range(len(words)):
        if j < len(words[i]):
            print(words[i][j], end='')