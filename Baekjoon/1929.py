def is_prime(n):
    if n == 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

N, M = map(int,input().split())

for x in range(N,M+1):
    if is_prime(x): print(x)