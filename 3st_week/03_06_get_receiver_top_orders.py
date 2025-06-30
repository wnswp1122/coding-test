top_heights = [6, 9, 5, 7, 4]

def get_receiver_top_orders(heights):
    stack = []  # [인덱스, 높이]를 저장
    answer = [0] * len(heights)
    
    for i in range(len(heights)):
        while stack and stack[-1][1] <= heights[i]:
            stack.pop()
        if stack:
            answer[i] = stack[-1][0] + 1
        stack.append([i, heights[i]])
    
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))