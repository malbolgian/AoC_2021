import numpy as np

class BingoBoard:
    def __init__(self, board: list[list[int]]):
        self.board = np.array(board)
        self.size = len(board)
        self.mask = self.board * 0
        self.won = False

    def update(self, num: int) -> bool:
        # Updates marked numbers (if necessary) and returns whether board wins
        if num not in self.board or self.won:
            return False
        row, col = np.where(self.board == num)
        row, col = row[0], col[0]
        self.mask[row][col] = 1
        
        # Only need to check row/col that includes updated position for win
        if np.sum(self.mask[row]) == self.size or np.sum(self.mask[:,col]) == self.size:
            self.won = True
        return self.won

    def sum_unmarked(self) -> int:
        return np.sum(self.board * (1 - self.mask))

def parse_input(input_path: str) -> tuple[list[int], list[BingoBoard]]:
    with open(input_path, 'r') as f:
        data = f.read().strip().split('\n\n')
        order = [int(i) for i in data[0].split(',')]
        boards = []
        for board_str in data[1:]:
            board_arr = [[int(i) for i in row.split()] for row in board_str.split('\n')]
            boards.append(BingoBoard(board_arr))
        return order, boards

def part1(data: tuple[list[int], list[BingoBoard]]) -> int:
    order, boards = data
    for num in order:
        for b in boards:
            if b.update(num):
                return b.sum_unmarked() * num

def part2(data: tuple[list[int], list[BingoBoard]]) -> int:
    order, boards = data
    total_won = 0
    for num in order:
        for b in boards:
            if b.update(num):
                total_won += 1
            if total_won == len(boards):
                return b.sum_unmarked() * num

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day04.txt')))
    print ('Part Two:', part2(parse_input('input/day04.txt')))
