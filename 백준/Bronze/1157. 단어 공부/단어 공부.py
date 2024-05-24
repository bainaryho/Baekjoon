word = input().upper()
uni_word = list(set(word))
cnt = []

for w in uni_word:
    cnt.append(word.count(w))

print("?") if cnt.count(max(cnt)) > 1 else print(uni_word[cnt.index(max(cnt))])
    
    
    


