import sys

N = int(sys.stdin.readline())
S = [sys.stdin.readline().strip() for _ in range(N)]
words = {} 

for s in S: 
    x = len(s)-1 
    
    for i in s :
        if i in words:
            words[i] += 10**x 
        else :
            words[i] = 10**x 
        x -= 1

words_sort = sorted(words.values(),reverse=True) 
result = 0
num = 9
for k in words_sort:
    result += k * num 
    num -= 1

print(result)
