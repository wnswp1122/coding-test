import sys
from collections import deque
input = sys.stdin.readline

K = input()
A = input().split()
max_num_arr = deque(map(str, range(10)))
min_num_arr = deque(map(str, range(10)))
max_result = ""
min_result = ""

stack = []
for inequality in A:
    if inequality == ">":
        p = max_num_arr.pop()
        max_result += p
        while len(stack) != 0:
            p = stack.pop()
            max_result += p
    elif inequality == "<":
        p = max_num_arr.pop()
        stack.append(p)
p = max_num_arr.pop()
max_result += p
while len(stack) != 0:
    p = stack.pop()
    max_result += p

stack = []
for inequality in A:
    if inequality == "<":
        p = min_num_arr.popleft()
        min_result += p
        while len(stack) != 0:
            p = stack.pop()
            min_result += p
    elif inequality == ">":
        p = min_num_arr.popleft()
        stack.append(p)
p = min_num_arr.popleft()
min_result += p
while len(stack) != 0:
    p = stack.pop()
    min_result += p

print(max_result)
print(min_result)