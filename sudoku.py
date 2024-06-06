import random

class Sudoku:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[0]*size for _ in range(size)]
        self.generate_grid()

    def generate_grid(self):
        def is_valid(num, row, col):
            for i in range(self.size):
                if self.grid[row][i] == num or self.grid[i][col] == num:
                    return False
            box_row, box_col = row - row % 2, col - col % 2
            for i in range(2):
                for j in range(2):
                    if self.grid[box_row + i][box_col + j] == num:
                        return False
            return True

        def fill():
            for row in range(self.size):
                for col in range(self.size):
                    if self.grid[row][col] == 0:
                        nums = list(range(1, self.size + 1))
                        random.shuffle(nums)
                        for num in nums:
                            if is_valid(num, row, col):
                                self.grid[row][col] = num
                                if fill():
                                    return True
                                self.grid[row][col] = 0
                        return False
            return True

        fill()
        self.remove_elements()

    def remove_elements(self):
        attempts = self.size * self.size // 2
        while attempts > 0:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            while self.grid[row][col] == 0:
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)
            backup = self.grid[row][col]
            self.grid[row][col] = 0

            grid_copy = [row[:] for row in self.grid]
            if not self.is_solvable(grid_copy):
                self.grid[row][col] = backup
                attempts -= 1
            else:
                attempts -= 1

    def is_solvable(self, grid):
        def is_valid(num, row, col):
            for i in range(self.size):
                if grid[row][i] == num or grid[i][col] == num:
                    return False
            box_row, box_col = row - row % 2, col - col % 2
            for i in range(2):
                for j in range(2):
                    if grid[box_row + i][box_col + j] == num:
                        return False
            return True

        def solve():
            for row in range(self.size):
                for col in range(self.size):
                    if grid[row][col] == 0:
                        for num in range(1, self.size + 1):
                            if is_valid(num, row, col):
                                grid[row][col] = num
                                if solve():
                                    return True
                                grid[row][col] = 0
                        return False
            return True

        return solve()

    def is_valid_move(self, num, row, col):
        if self.grid[row][col] != 0:
            return False
        for i in range(self.size):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        box_row, box_col = row - row % 2, col - col % 2
        for i in range(2):
            for j in range(2):
                if self.grid[box_row + i][box_col + j] == num:
                    return False
        return True

    def make_move(self, num, row, col):
        if self.is_valid_move(num, row, col):
            self.grid[row][col] = num
            return True
        return False

    def is_solved(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == 0:
                    return False
        return True
