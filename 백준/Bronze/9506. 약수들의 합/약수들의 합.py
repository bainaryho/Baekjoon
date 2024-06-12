while True:
    n = int(input())
    num_list = []
    
    if n == -1:
        break
        
    for i in range(1, n//2+1):
        if n % i == 0:
            num_list.append(i)
    
    if sum(num_list) == n:
        print(n, "=", end=" ")
        print(*num_list, sep=" + ")
    else:
        print(n, "is NOT perfect.")