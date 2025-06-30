def kaing(M,N,x,y):
    if M > N: year = x
    else: year = y
    while M*N >= year:
        if (year - x) % M == 0 and (year - y) % N == 0:
            return year
        year += max(M,N)
    return -1

N = int(input())
for i in range(N):
    M,N,x,y = map(int,input().split())
    print(kaing(M,N,x,y))
    
