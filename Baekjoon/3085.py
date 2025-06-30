n = int(input())

c = []
for _ in range(n):
    candies = list(map(str, input()))
    c.append(candies)


def checkCurMaxNum():
    max_cnt = 1  # total_max_cnt
    for i in range(n):
        # 가로 먼저 확인
        cnt = 1
        for j in range(1, n):
            if c[i][j] == c[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
        # 세로 확인
        cnt = 1
        for j in range(1, n):
            if c[j][i] == c[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)

    return max_cnt


# 오른쪽 swap, 아래쪽 swap
result = 1
for i in range(n):
    for j in range(n - 1):
        # 오른쪽 swap
        if j + 1 < n and c[i][j] != c[i][j + 1]:
            c[i][j], c[i][j + 1] = c[i][j + 1], c[i][j]  # swap
            # 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분을 고름
            result = max(result, checkCurMaxNum())
            c[i][j], c[i][j + 1] = c[i][j + 1], c[i][j]  # 다시 되돌리기
        # 왼쪽 swap
        if i + 1 < n and c[i][j] != c[i + 1][j]:
            c[i][j], c[i + 1][j] = c[i + 1][j], c[i][j]  # swap
            # 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분을 고름
            result = max(result, checkCurMaxNum())
            c[i][j], c[i + 1][j] = c[i + 1][j], c[i][j]  # 다시 되돌리기

print(result)