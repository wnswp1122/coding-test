import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
used = [False] * N
min_cost = float('inf')

def permutation(path, used):
    global min_cost
    if len(path) == N:
        cost = calculate_cost(path)
        if cost:
            min_cost = min(cost, min_cost)
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            permutation(path + [i], used)
            used[i] = False

def calculate_cost(path):
    cost = 0
    for i in range(N-1):
        if W[path[i]][path[i+1]] == 0:
            return False
        cost += W[path[i]][path[i+1]]
    if W[path[N-1]][path[0]] == 0:
        return False
    return cost + W[path[N-1]][path[0]]

permutation([], used)
print(min_cost)
