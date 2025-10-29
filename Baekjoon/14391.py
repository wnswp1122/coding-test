N, M = map(int, input().split())
paper = [list(map(int, list(input().strip()))) for _ in range(N)]

max_sum = 0

for bit in range(1 << (N * M)):  # 2^(N*M) 가지 모든 경우의 수
    total = 0

    # 가로 조각 계산
    for i in range(N):
        row_sum = 0
        for j in range(M):
            idx = i * M + j
            if (bit & (1 << idx)) == 0:  # 가로 조각인 경우
                row_sum = row_sum * 10 + paper[i][j]
            else:
                total += row_sum
                row_sum = 0
        total += row_sum  # 마지막 조각 처리

    # 세로 조각 계산
    for j in range(M):
        col_sum = 0
        for i in range(N):
            idx = i * M + j
            if (bit & (1 << idx)) != 0:  # 세로 조각인 경우
                col_sum = col_sum * 10 + paper[i][j]
            else:
                total += col_sum
                col_sum = 0
        total += col_sum  # 마지막 조각 처리

    max_sum = max(max_sum, total)

print(max_sum)
