import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []

def backtrack():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, N + 1):
        result.append(i)
        backtrack()
        result.pop()

backtrack()