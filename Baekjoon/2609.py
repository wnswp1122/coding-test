a, b = map(int, input().split())

def GCD(a,b):
    while b:
        a, b = b, a%b   
    return a

def LCM(a,b):
    return a * b // GCD(a,b)

print(GCD(a,b))
print(LCM(a,b))