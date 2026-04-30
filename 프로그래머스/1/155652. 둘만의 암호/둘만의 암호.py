def solution(s, skip, index):
    answer = ""
    alphabet = [char for char in "abcdefghijklmnopqrstuvwxyz" if char not in skip]
    n = len(alphabet)
    
    for char in s:
        current_idx = alphabet.index(char)
        new_idx = (current_idx + index) % n
        answer += alphabet[new_idx]
        
    return answer