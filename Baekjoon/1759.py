import sys
input = sys.stdin.readline

L, C = map(int, input().split())
chars = input().split()
chars.sort()  # 오름차순 정렬

vowels = {'a', 'e', 'i', 'o', 'u'}

def is_valid(password):
    vowel_count = sum(1 for ch in password if ch in vowels)
    consonant_count = len(password) - vowel_count
    return vowel_count >= 1 and consonant_count >= 2

def backtrack(start, password):
    if len(password) == L:
        if is_valid(password):
            print("".join(password))    
        return

    for i in range(start, C):
        backtrack(i + 1, password + [chars[i]])

# 실행
backtrack(0, [])
