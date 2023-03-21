def solution(n, m, s):
    answer = 0
    temp = 0
    for i in range(len(s)):
        if s[i]<=temp:
            continue
        else:
            answer+=1
            temp = s[i]+m-1
    return answer