def is_correct_parenthesis(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(True)
        elif string[i] == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))