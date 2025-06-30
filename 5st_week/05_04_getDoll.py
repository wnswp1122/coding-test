def solution(board, moves):
    n = len(board)
    doll_arr = []
    for move in moves:
        for i in range(n):
            if board[i][move - 1] != 0:
                doll_arr.append(board[i][move - 1])
                board[i][move - 1] = 0
                break
    
    answer = 0
    check = True
    while check:
        check = False
        for i in range(len(doll_arr) - 1):
            if doll_arr[i] == doll_arr[i + 1]:
                del doll_arr[i:i+2]
                check = True
                answer += 2
                break
            
    return answer

        



        