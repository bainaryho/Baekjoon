import sys
N, M = map(int, input().split())
basket = [0]*N
for _ in range(M):
    i,j,k = map(int, sys.stdin.readline().split())
    for n in range(i,j+1):
        basket[n-1] = k
        
for i in range(N):
    print(basket[i],end=' ')
