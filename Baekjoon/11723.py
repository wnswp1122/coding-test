import sys
input = sys.stdin.readline

N = int(input())
S = set()
for _ in range(N):
    op, *rest = input().split()
    num = int(rest[0]) if rest else None

    if op == "add":
        S.add(num)
    elif op == "remove":
        S.discard(num)
    elif op == "check":
        if num in S: print(1)
        else: print(0)
    elif op == "toggle":
        if num in S: S.discard(num)
        else: S.add(num)
    elif op == "all":
        S.clear()
        S = set(range(1,21))
    elif op == "empty":
        S.clear()

