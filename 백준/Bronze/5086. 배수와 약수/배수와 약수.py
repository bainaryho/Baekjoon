while True:
    num1, num2 = map(int,input().split())
    #각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를,
    #배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.
    if num1 == 0 and num2 == 0:
        break
    elif num2 % num1 == 0:
        print("factor")
    elif num1 % num2 == 0:
        print("multiple")
    else:
        print("neither")
