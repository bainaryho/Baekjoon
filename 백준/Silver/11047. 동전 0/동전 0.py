a,price = map(int,input().split())
coin = []
for _ in range(a):
    coin.append(int(input()))
coin.sort(reverse=True)

result = 0
for i in coin:
        result += price//i
        price = price%i
print(result)