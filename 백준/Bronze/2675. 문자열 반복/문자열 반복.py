T = int(input())
for i in range(T):
    num, S = input().split()
    num = int(num)
    S = str(S)
    for i in range(len(S)):
        print(S[i]*num, end="")
    print()