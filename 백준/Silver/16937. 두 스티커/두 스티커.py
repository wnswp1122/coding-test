import sys
input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())
stickers = [tuple(map(int, input().split())) for _ in range(N)]

def can_place(r1, c1, r2, c2):
    if r1 + r2 <= H and max(c1, c2) <= W:
        return True
    if max(r1, r2) <= H and c1 + c2 <= W:
        return True
    return False

answer = 0

for i in range(N):
    for j in range(i + 1, N):
        r1, c1 = stickers[i]
        r2, c2 = stickers[j]
        for a, b in [(r1, c1), (c1, r1)]:
            for c, d in [(r2, c2), (c2, r2)]:
                if can_place(a, b, c, d):
                    answer = max(answer, a * b + c * d)

print(answer)