def is_number_exist(number, number_list):
    for num in number_list:
        if num == number:
            return True
    return False

result = is_number_exist
print(result(5, [1, 2, 3, 4, 5])) # 연산량 많아짐짐
print(result(1, [1, 2, 3, 4, 5]))  # 연산량 적음