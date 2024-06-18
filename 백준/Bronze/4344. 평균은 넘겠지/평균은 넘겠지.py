# 입력을 받기 위해 sys 모듈을 임포트합니다.
import sys
input = sys.stdin.read

# 입력을 한 번에 받습니다.
data = input().strip().split('\n')

# 첫 번째 줄은 테스트 케이스의 개수 C입니다.
C = int(data[0])

# 결과를 저장할 리스트를 초기화합니다.
results = []

# 각 테스트 케이스에 대해 반복합니다.
for i in range(1, C + 1):
    # 현재 테스트 케이스의 데이터를 공백을 기준으로 나눕니다.
    case = list(map(int, data[i].split()))
    
    # 첫 번째 숫자는 학생의 수 N입니다.
    N = case[0]
    
    # 나머지 숫자는 학생들의 점수입니다.
    scores = case[1:]
    
    # 평균을 계산합니다.
    avg = sum(scores) / N
    
    # 평균을 넘는 학생 수를 계산합니다.
    count_above_avg = sum(1 for score in scores if score > avg)
    
    # 평균을 넘는 학생들의 비율을 계산합니다.
    percentage_above_avg = (count_above_avg / N) * 100
    
    # 결과를 소수점 셋째 자리까지 반올림하여 저장합니다.
    results.append(f"{percentage_above_avg:.3f}%")

# 결과를 출력합니다.
for result in results:
    print(result)