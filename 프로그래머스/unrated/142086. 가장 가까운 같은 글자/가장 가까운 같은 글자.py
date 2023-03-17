def solution(s):
    answer = []
    rdict = {}
    for i in range (len(s)):
        word = s[i]
        if word in rdict:
            answer.append(i-rdict[word])
        else : 
            answer.append(-1)
        rdict[word] = i
    return answer