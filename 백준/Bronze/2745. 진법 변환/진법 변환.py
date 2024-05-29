def convert_to_decimal(N, B):
    # int 함수에 문자열과 진법을 넘겨주면 10진수로 변환됩니다.
    decimal_value = int(N, B)
    return decimal_value

# 입력 받기
N, B = input().split()
B = int(B)

# 변환 및 출력
print(convert_to_decimal(N, B))