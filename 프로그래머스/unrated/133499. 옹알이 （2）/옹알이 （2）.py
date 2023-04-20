def solution(babbling):
    answer = 0
    for bab in babbling:
        for word in ["aya", "ye", "woo", "ma"]:
            if word*2 not in bab:
                bab=bab.replace(word,' ')
        if len(bab.strip())==0:
            answer +=1
    return answer