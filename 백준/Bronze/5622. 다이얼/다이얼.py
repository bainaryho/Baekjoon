num = list(input())
number = ['ABC',"DEF",'GHI',"JKL","MNO","PQRS","TUV","WXYZ"]
result = 0
for i in num:
    for j in number:
        if i in j:
            result += number.index(j)+3

print(result)