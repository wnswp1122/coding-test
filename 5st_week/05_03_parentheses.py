from collections import deque

balanced_parentheses_string = "()))((()"

def is_balanced(string):
    if string.count("(") == string.count(")"):
        return True
    else: return False

def is_correct(string):
    stack = deque()
    for char in string:
        if char == "(":
            stack.append(char)
        else:  # char == ")"
            if not stack:  # 스택이 비어있다면
                return False
            stack.pop()  # 스택에서 마지막 원소 제거
    return len(stack) == 0  # 스택이 비어있으면 올바른 괄호 문자열

def get_correct_parentheses(balanced_parentheses_string):
    if balanced_parentheses_string == "":
        return ""
    u = ""
    v = ""
    for i in range(len(balanced_parentheses_string)):
        u += balanced_parentheses_string[i]
        if is_balanced(u):
            v = balanced_parentheses_string[i + 1:]
            break

    if is_correct(u):
        return u + get_correct_parentheses(v)
    else:
        e = "("
        e += get_correct_parentheses(v) + ")"
        u = u[1:-1]
        for char in u:
            if char == "(":
                e += ")"
            else:
                e += "("
        return e

