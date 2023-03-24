def solution(s):
    answer = 0
    countx = 0
    other = 0
    for letter in s:
        if countx == other:
            answer +=1
            x=letter
        if letter==x:
            countx+=1
        else:
            other+=1
        
    return answer