def next_permutation(arr):
    N = len(arr)
    
    # 1. i-1 찾기
    i = N - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    
    if i == 0:
        return False  # 마지막 순열

    # 2. j 찾기 (i-1보다 큰 값 중 맨 뒤에서부터)
    j = N - 1
    while arr[i - 1] >= arr[j]:
        j -= 1

    # 3. swap
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # 4. i부터 끝까지 뒤집기
    arr[i:] = reversed(arr[i:])
    
    return True


# 입력 처리
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

if next_permutation(arr):
    print(' '.join(map(str, arr)))
else:
    print(-1)

