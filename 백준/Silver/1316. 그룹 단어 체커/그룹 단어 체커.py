def is_group_word(word):
    word_set = set() #이미 등장한 문자 저장 집합
    last_char = ''
    for char in word:
        if char != last_char:
            if char in word_set:
                return False # 그룹단어 아님
            word_set.add(char)
        last_char = char
    return True    
    
N = int(input())
words = [input().strip() for _ in range(N)] #입력

#is_group_word(word)가 True인 경우에만 1, sum 함수를 통해 이 값들을 모두 더함
print(sum(1 for word in words if is_group_word(word)))

#그룹 단어 개수 세기
#result = 0
#for word in words:
#    if is_group_word(word):
#        result += 1
#print(result)
    