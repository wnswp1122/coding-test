N = int(input())
d = len(str(N))

if N < 10:
    print(N)
else:
    answer = 0
    for i in range(1,d):
        answer += (9 * (10 ** (i - 1))) * i
    answer += ((N - (10 ** (d-1))) + 1) * d
    print(answer)
    