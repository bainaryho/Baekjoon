def solution(t, p):
    lent = len(t)+1
    lenp = len(p)
    p = int(p)
    answer = 0
    
    for i in range(0,lent-lenp):
        if int(t[i:lenp+i]) <= p :
            answer += 1
    
    return answer