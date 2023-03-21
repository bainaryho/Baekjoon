def solution(wall):
    lX,lY = [],[]
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == '#':
                lX.append(i)
                lY.append(j)
    return [min(lX),min(lY),max(lX)+1,max(lY)+1]
                   