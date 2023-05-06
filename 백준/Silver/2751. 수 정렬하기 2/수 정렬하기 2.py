import sys
input=sys.stdin.readline

a = int(input())
li = []
for i in range(a):
    li.append(int(input()))

li = sorted(li)
for i in li:
    print(i)