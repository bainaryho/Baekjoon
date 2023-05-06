n = int(input())

coordinate = []

for _ in range(n):
    coordinate.append(list(map(int, input().split())))

coordinate.sort()

for i in coordinate:
    print(i[0], i[1])