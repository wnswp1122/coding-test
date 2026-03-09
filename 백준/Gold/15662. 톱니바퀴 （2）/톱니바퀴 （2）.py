from collections import deque
import sys
input = sys.stdin.readline

sawtooth = []
T = int(input())

for _ in range(T):
    sawtooth.append(deque(map(int, input().strip())))

K = int(input())

for _ in range(K):
    n, dir = map(int,input().split())
    n -= 1

    rotate_dir = [0] * T
    rotate_dir[n] = dir

    for i in range(n, T-1):
        if sawtooth[i][2] != sawtooth[i+1][6]:
            rotate_dir[i+1] = -rotate_dir[i]
        else:
            break

    for i in range(n, 0, -1):
        if sawtooth[i][6] != sawtooth[i-1][2]:
            rotate_dir[i-1] = -rotate_dir[i]
        else:
            break
    for i in range(T):
        if rotate_dir[i] != 0:
            sawtooth[i].rotate(rotate_dir[i])

print(sum(s[0] for s in sawtooth))