num = int(input())
arr = [int(input()) for _ in range(num)]
arr.sort()

arr_sum = set()

# 두 수의 합을 구하는데 중복 계산을 없앰
for i in range(num):
    for j in range(i, num):
        arr_sum.add(arr[i] + arr[j])

def check():
    global answer
    # 큰 수부터 확인하여 가장 큰 값을 찾으면 바로 리턴
    for i in range(num - 1, -1, -1):
        for j in range(i + 1):
            if arr[i] - arr[j] in arr_sum:
                return arr[i]

answer = check()
print(answer)