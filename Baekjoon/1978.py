def is_prime(number):
    if number == 1: return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

n = int(input())
nums = list(map(int, input().split()))
count = 0

for num in nums:
    if is_prime(num):
        count += 1

print(count) 
        




