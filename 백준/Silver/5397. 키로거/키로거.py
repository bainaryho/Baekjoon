import sys
input = sys.stdin.readline
num = int(input())

for i in range(num):
    password = list(input().strip())
    left, right = [], []

    for j in password:
        if j == '<':
            if left:  # left가 비어있지 않으면 -> 커서가 이동가능하면
                right.append(left.pop())
        elif j == '>':
            if right:  # 커서가 이동가능하면
                left.append(right.pop())
        elif j == '-':
            if left:  # 삭제할 문제가 있으면
                left.pop()
        else:
            left.append(j)

    left.extend(reversed(right))

    print(''.join(left))