import tkinter as tk
from tkinter import messagebox
from sudoku import Sudoku

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("4x4 Sudoku")
        self.sudoku = Sudoku()
        self.entries = [[None]*4 for _ in range(4)]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        for row in range(4):
            for col in range(4):
                self.entries[row][col] = tk.Entry(self.root, width=5, font=('Arial', 18), justify='center')
                self.entries[row][col].grid(row=row, column=col, padx=5, pady=5)
                if self.sudoku.grid[row][col] != 0:
                    self.entries[row][col].insert(0, self.sudoku.grid[row][col])
                    self.entries[row][col].config(state='disabled')

    def create_buttons(self):
        check_button = tk.Button(self.root, text="Check", command=self.check_solution)
        check_button.grid(row=4, column=0, columnspan=2, pady=10)

        reset_button = tk.Button(self.root, text="Reset", command=self.reset_grid)
        reset_button.grid(row=4, column=2, columnspan=2, pady=10)

    def check_solution(self):
        for row in range(4):
            for col in range(4):
                entry = self.entries[row][col].get()
                if entry == '':
                    messagebox.showerror("Error", "All cells must be filled")
                    return
                if not entry.isdigit():
                    messagebox.showerror("Error", "All entries must be numbers")
                    return
                num = int(entry)
                if not (1 <= num <= 4):
                    messagebox.showerror("Error", "Numbers must be between 1 and 4")
                    return
                self.sudoku.grid[row][col] = num

        if self.is_correct_solution():
            messagebox.showinfo("Success", "Congratulations! You solved the puzzle.")
        else:
            messagebox.showerror("Error", "The puzzle is not solved correctly.")

    def is_correct_solution(self):
        # Check rows and columns
        for i in range(4):
            row_set = set()
            col_set = set()
            for j in range(4):
                row_set.add(self.sudoku.grid[i][j])
                col_set.add(self.sudoku.grid[j][i])
            if len(row_set) != 4 or len(col_set) != 4:
                return False

        # Check 2x2 subgrids
        for box_row in range(0, 4, 2):
            for box_col in range(0, 4, 2):
                box_set = set()
                for i in range(2):
                    for j in range(2):
                        box_set.add(self.sudoku.grid[box_row + i][box_col + j])
                if len(box_set) != 4:
                    return False

        return True

    def reset_grid(self):
        self.sudoku = Sudoku()  # Reset the Sudoku grid
        for row in range(4):
            for col in range(4):
                self.entries[row][col].config(state='normal')
                self.entries[row][col].delete(0, tk.END)
                if self.sudoku.grid[row][col] != 0:
                    self.entries[row][col].insert(0, self.sudoku.grid[row][col])
                    self.entries[row][col].config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
