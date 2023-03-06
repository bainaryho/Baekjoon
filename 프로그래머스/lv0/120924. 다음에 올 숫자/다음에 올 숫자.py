def solution(common):
    answer = 0
    n = int(common[1]) - int(common[0])
    if n == int(common[2])-int(common[1]):
        answer = int(common[-1])+n
    else :
        answer = (common[1]/common[0]) * common[-1]
    return answer