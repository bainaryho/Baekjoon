def solution(s):
    count = 0
    for x in s:
        if x == '(':
            count += 1
        else:
            if count>0:
                count -= 1
            else :
                return False
    return count == 0
        
        