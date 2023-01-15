from sys import stdin

score = []
result = []
maxnum = 0

for i in range(8):
    score.append(int(stdin.readline()))

for i in range(5):
    maxnum += max(score)
    idx = score.index(max(score))
    result.append(idx+1)
    score[idx] = 0
    
print(maxnum)
print(*(sorted(result)))
