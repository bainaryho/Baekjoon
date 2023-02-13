n = int(input())
nums = input()
result = 0

nums = list(nums)

for i in range(n):
    result += int(nums[i])
    
print(result)