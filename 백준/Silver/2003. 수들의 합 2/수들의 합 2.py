import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
left = 0
total = 0

for right in range(n):
    total += arr[right]
    while total > m:
        total -= arr[left]
        left += 1
    if total == m:
        count += 1

print(count)