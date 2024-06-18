import sys
input = sys.stdin.read
data = input().strip().split('\n')
C = int(data[0])
results = []
for i in range(1, C + 1):
    case = list(map(int, data[i].split()))
    N = case[0]
    scores = case[1:]
    avg = sum(scores) / N
    count_above_avg = sum(1 for score in scores if score > avg)
    percentage_above_avg = (count_above_avg / N) * 100
    results.append(f"{percentage_above_avg:.3f}%")

for result in results:
    print(result)