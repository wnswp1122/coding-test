import sys
input = sys.stdin.readline

def lotto_strategy(nums, path, start):
    if len(path) == 6:
        print(' '.join(map(str, path)))
        return

    for i in range(start, len(nums)):
        lotto_strategy(nums, path + [nums[i]], i + 1)

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    nums = data[1:]
    lotto_strategy(nums, [], 0)
    print()  # 테스트 케이스 구분을 위한 공백
