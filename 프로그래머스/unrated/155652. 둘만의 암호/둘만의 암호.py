def solution(s, skip, index):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for letter in skip:
        alphabet.remove(letter)

    slist = list(s)
    for i in range(len(slist)):
        if slist[i] not in skip:
            old_index = alphabet.index(slist[i])
            new_index = (old_index + index) % len(alphabet)
            slist[i] = alphabet[new_index]
    
    result = ''.join(slist)
    return result