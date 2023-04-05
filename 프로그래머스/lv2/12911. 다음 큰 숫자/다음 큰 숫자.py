def solution(n):
    num1 = ['',0,0] #0번:2진법 1번:1의개수 2번:정수
    num2 = ['',0] #0번:2진법 1번:1의개수
    num1[0] = bin(n)[2:]
    num1[1] = num1[0].count('1')
    num1[2] = n
    n2 = n+1
    
    while 1:
        num2[0] = bin(n2)[2:]
        num2[1] = num2[0].count('1')
        if num1[1] == num2[1]:
            return n2
        else:
            n2 += 1
        
    