def solution(keymap, targets):
    answer = []
    keyNum = {}
    for keys in keymap:
        for i,key in enumerate(keys):
            if key not in keyNum:
                keyNum[key] = i+1
            else:
                keyNum[key] = min(keyNum[key], i + 1)
                
    for target in targets:
        result = 0
        for key in target:
            if key not in keyNum:
                result = -1
                break
            result += keyNum[key]
            
        answer.append(result)
    return answer