N = int(input())
arr = list(map(int, input().split()))   

used = [False] * N
max_diff = 0

def calculate_diff(arr):
    total = 0
    for i in range(len(arr) - 1):
        total += abs(arr[i] - arr[i + 1])
    return total
def permutation(path, used, nums):
    global max_diff
    
    if len(path) == N:
        diff = calculate_diff(path)
        max_diff = max(max_diff, diff)
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            permutation(path + [nums[i]], used, nums)
            used[i] = False

permutation([], used, arr)
print(max_diff)