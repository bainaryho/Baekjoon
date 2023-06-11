import sys
N, M = map(int,input().split())
bs = [i for i in range(1,N+1)]

for n in range(M):
    i,j = map(int, sys.stdin.readline().split())
    bs[i-1],bs[j-1] = bs[j-1],bs[i-1]

for n in range(N):
    print(bs[n],end=' ')
    