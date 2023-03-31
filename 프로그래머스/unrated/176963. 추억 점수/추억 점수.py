def solution(name, yearning, photos):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]

    for photo in photos:
        result=0
        for p in photo:
            if type(dic.get(p)) == int:
                result += dic.get(p)
        answer.append(result)
    
    return answer