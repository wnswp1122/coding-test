E,S,M = map(int,input().split())

# 15 28 19
N = E
while True:
    if (N - S) % 28 == 0:
        while True:
            if (N - M) % 19 == 0:
                print(N)
                exit(0)
            else: N += 15 * 28
    else: N += 15

            
    