def summarize_string(input_str):
    answer = ""
    count = 0
    for i in range(len(input_str) - 1):
        if input_str[i] == input_str[i+1]:
            count += 1
        else:
            answer += input_str[i] + str(count + 1)
            count = 0
    answer += input_str[i] + str(count + 1)
    return answer    

input_str = "acccdeee"

print(summarize_string(input_str))