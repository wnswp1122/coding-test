import sys
input = sys.stdin.readline

N = int(input())
nums = [1, 5, 10, 50]
s = {0}

for _ in range(N):
    temp = set()
    for v in s:
        for n in nums:
            temp.add(v + n)
    s = temp

print(len(s))