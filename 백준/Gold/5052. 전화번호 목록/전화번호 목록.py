def is_consistent(phone_numbers):
    phone_numbers.sort()
    for i in range(len(phone_numbers) - 1):
        if phone_numbers[i + 1][:len(phone_numbers[i])] == phone_numbers[i]:
            return "NO"
    return "YES"

tests = int(input())
for i in range(tests):
    cases = int(input())
    phone_numbers = []
    for i in range(int(cases)):
        phone_numbers.append(input())
        
    result = is_consistent(phone_numbers)
    print(result)