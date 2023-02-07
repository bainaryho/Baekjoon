num1 = int(input())
num2 = int(input())
num3 = int(input())

nums = list(str(num1 * num2 * num3))

result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in nums:
    result[int(i)] += 1
    
for i in result:
    print(i)