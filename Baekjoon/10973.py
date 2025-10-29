def prev_permutation(arr):
    N = len(arr)
    i = N - 1
    while i > 0 and arr[i] >= arr[i-1]:
        i -= 1
    if i == 0: return False

    j = N - 1
    while arr[i - 1] <= arr[j]:    
        j -= 1

    arr[i-1], arr[j] = arr[j], arr[i-1]
    arr[i:] = reversed(arr[i:])
    return True

# 입력 처리
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

if prev_permutation(arr):
    print(' '.join(map(str, arr)))
else:
    print(-1)

