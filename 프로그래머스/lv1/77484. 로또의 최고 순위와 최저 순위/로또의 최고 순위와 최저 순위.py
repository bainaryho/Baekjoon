def solution(lottos, nums):
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6} # 순위와 당첨 내용 딕셔너리
    error = lottos.count(0) #낙서된 번호의 갯수(추후 최고순위에 +됨)
    count = error
    
    for i in range(len(lottos)):
        if lottos[i] in nums:
            count += 1
    
    return [rank[count],rank[count-error]]