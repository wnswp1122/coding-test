import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []

def backtrack(start):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, N + 1):
        result.append(i)
        backtrack(i)
        result.pop()

backtrack(1)