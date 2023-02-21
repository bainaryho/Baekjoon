#start = input()
#num = start
#cnt = 0 #카운트
#result = 0

#while 1:
#    if len(num)==1:
#        num = "0"+num
#    result = str(int(num[0])+int(num[1]))
#    num = num[-1]+result[-1]
#    cnt += 1
#    if num==start:
#        print(cnt)
#        break

n = int(input()) 
num = n
count = 0

while True:
    a = num//10 
    b = num%10 
    c = (a+b)%10 
    num = (b*10)+c 
    
    count+=1
    if(num==n):
        break

print(count)