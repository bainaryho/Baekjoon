check_pd = input()
is_palindrome = True

for i in range(len(check_pd) // 2):
    if check_pd[i] != check_pd[-1-i]:
        is_palindrome = False  
        break

print(1) if is_palindrome else print(0)