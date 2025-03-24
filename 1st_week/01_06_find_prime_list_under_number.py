input = 20


def find_prime_list_under_number(number):
    prime_arr = []
    for i in range(2, number+1):
        for x in prime_arr:
            if i % x == 0 and x * x <= number: break
        else: prime_arr.append(i)

    return prime_arr


result = find_prime_list_under_number(input)
print(result)