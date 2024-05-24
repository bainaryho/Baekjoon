check_pd = input()
minus = -1
is_palindrome = True

for i in range(len(check_pd) // 2):
    if check_pd[i] != check_pd[minus]:
        is_palindrome = False  
        break
    minus -= 1

if is_palindrome:
    print("1")
else:
    print("0")