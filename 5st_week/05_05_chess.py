import sys
input = sys.stdin.readline

# 방향 인덱스 (0-based) : 0=오른쪽,1=왼쪽,2=위,3=아래
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def reverse_dir(d):
    return [1, 0, 3, 2][d]

class Cell:
    def __init__(self, color):
        self.color = color    # 0,1,2
        self.horses = []      # 말 번호 리스트, 아래 -> 위 순서

    def add_horses(self, horses):
        self.horses.extend(horses)

    def remove_horses_from(self, horse_num):
        idx = self.horses.index(horse_num)
        moving = self.horses[idx:]
        self.horses = self.horses[:idx]
        return moving

    def count(self):
        return len(self.horses)

class Game:
    def __init__(self, N, K, board_color, horses_info):
        self.N = N
        self.K = K
        self.board = [[Cell(board_color[r][c]) for c in range(N)] for r in range(N)]
        # horse_info: horse_num -> [r,c,d]
        self.horse_info = {}
        for i, (r, c, d) in enumerate(horses_info, 1):
            self.horse_info[i] = [r-1, c-1, d-1]
            self.board[r-1][c-1].add_horses([i])
        self.game_over = False  # 게임 종료 상태 초기화

    def move_horse(self, horse_num):
        r, c, d = self.horse_info[horse_num]
        cell = self.board[r][c]

        moving = cell.remove_horses_from(horse_num)

        nr, nc = r + dr[d], c + dc[d]

        # 범위 밖 또는 파란색 칸 처리
        if not (0 <= nr < self.N and 0 <= nc < self.N) or self.board[nr][nc].color == 2:
            d = reverse_dir(d)
            self.horse_info[horse_num][2] = d
            nr, nc = r + dr[d], c + dc[d]

            if not (0 <= nr < self.N and 0 <= nc < self.N) or self.board[nr][nc].color == 2:
                cell.add_horses(moving)
                return

        dest_cell = self.board[nr][nc]

        if dest_cell.color == 1:
            moving.reverse()

        for hn in moving:
            self.horse_info[hn][0], self.horse_info[hn][1] = nr, nc

        dest_cell.add_horses(moving)

        # 이동한 칸만 검사
        if dest_cell.count() >= 4:
            self.game_over = True

    def simulate(self):
        turn = 0
        while turn < 1000:
            turn += 1
            for horse_num in range(1, self.K + 1):
                self.move_horse(horse_num)
                if self.game_over:
                    return turn
        return -1

# 입력 처리
N, K = map(int, input().split())
board_color = [list(map(int, input().split())) for _ in range(N)]
horses_info = [tuple(map(int, input().split())) for _ in range(K)]

game = Game(N, K, board_color, horses_info)
print(game.simulate())
