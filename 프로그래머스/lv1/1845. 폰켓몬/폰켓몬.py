def solution(nums):
    count = len(nums)/2
    answer = list(set(nums))
    if len(answer) > count:
        return count
    else :
        return len(answer)
    