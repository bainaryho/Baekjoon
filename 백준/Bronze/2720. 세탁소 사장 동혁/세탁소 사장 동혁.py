def calculate_coins(cents):
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents
    return quarters, dimes, nickels, pennies

# 입력 받기
T = int(input())
test_cases = [int(input()) for _ in range(T)]

# 각 테스트 케이스에 대해 결과 출력
for cents in test_cases:
    q, d, n, p = calculate_coins(cents)
    print(q, d, n, p)