def Eratos(n):
    array = [True for i in range(n)]
    i = 2
    while i * i <= n:
        if array[i]:
            j = 2
            while i * j < n:
                array[i * j] = False
                j += 1
        i += 1
    del array[0:3]
    return array

def Goldbach(arr):
    prime_arr = Eratos(max(arr))
    for n in arr:
        for index in range(len(prime_arr)):
            if prime_arr[index] == True:
                if prime_arr[n - index - 6] == True:
                    print("{} = {} + {}".format(n,index+3,n-index-3))
                    break


import sys
#sys 이용해야 시간초과 안나게 할 수 있음
input_arr = []

while True:
    N = int(sys.stdin.readline())
    if N == 0: break
    input_arr.append(N)

Goldbach(input_arr)
