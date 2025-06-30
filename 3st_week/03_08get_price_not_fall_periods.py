from collections import deque

prices = [1, 2, 3, 2, 3]


def get_price_not_fall_periods(prices):
    result = []
    prices = deque(prices)

    while prices:
        price_not_fall_period = 0
        current_price = prices.popleft()
        for next_price in prices:
            if current_price > next_price:
                price_not_fall_period += 1
                break
            price_not_fall_period += 1

        result.append(price_not_fall_period)

    return result


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))
