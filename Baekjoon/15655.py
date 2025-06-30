N, M = map(int, input().split())
numbers = [int(x) for x in input().split()]
numbers.sort()

result = []

def backtrack(start):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(N):
        if numbers[i] in result or (result and max(result) > numbers[i]):
            continue
        result.append(numbers[i])
        backtrack(i)
        result.pop()

backtrack(0)