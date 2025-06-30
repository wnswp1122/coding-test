N, M = map(int, input().split())
numbers = [int(x) for x in input().split()]
numbers.sort()

result = []

def backtrack():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(N):
        if numbers[i] in result:
            continue
        result.append(numbers[i])
        backtrack()
        result.pop()

backtrack()