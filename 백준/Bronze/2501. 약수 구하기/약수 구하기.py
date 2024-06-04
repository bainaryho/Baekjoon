N, K = map(int,input().split())
yak_su = []
for i in range(1, N + 1):
    if (N % i == 0) :
        yak_su.append(i)
if len(yak_su) < K :	
    print(0)
else :
    print(yak_su[K-1])