dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
# 동 서 북 남
# →, ←, ↑, ↓
#0은 흰색, 1은 빨간색, 2는 파란색
def horse_move(horse):
    horse[0], horse[1] = horse[0] + dr[horse[2]], horse[1] + dc[horse[2]]
    return horse

        
def get_game_over_turn_count(horse_count, game_map, horse_info):
    horse_stack = [] * horse_count
    # [3 2 0] [0 0 0] [2 0 0] [5 0 0] [0 0 0] 1 3 2 , 4 5
    for i in range(horse_count):
        horse_move(horse_info[i])
        #앞의 색깔,말
        
        #스택쌓기 -> 반복문 돌면서 count >= 4면 중지 , 스택을 하나로 

k = 4  # 말의 개수  

chess_map = [
    [0, 0, 2, 0],
    [0, 0, 1, 0],   
    [0, 0, 1, 2],
    [0, 2, 0, 0]
]
start_horse_info = [
    [1, 0, 0],
    [2, 1, 2],
    [1, 1, 0],
    [3, 0, 1]
]

get_game_over_turn_count(k,chess_map,start_horse_info)