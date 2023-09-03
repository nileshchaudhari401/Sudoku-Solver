import tkinter as tk

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.create_grid()
        self.create_menu()

    def create_grid(self):
        self.cells = [[tk.StringVar() for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                frame = tk.Frame(self.root, padx=2, pady=2, bd=1)
                frame.grid(row=i, column=j)
                entry = tk.Entry(frame, textvariable=self.cells[i][j], width=5, font=("Arial", 15))
                entry.pack(fill=tk.BOTH, expand=True)
                entry.bind("<FocusIn>", lambda event, i=i, j=j: self.highlight_box(i, j))
                self.entries[i][j] = entry

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.quit)
        file_menu.add_command(label="Solve", command=self.solve_sudoku)
        file_menu.add_command(label="Clear", command=self.clear_grid)

    def clear_grid(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].set('')
                self.entries[i][j].config(bg='white')  

    def highlight_box(self, row, col):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].config(bg='gray')  
        for i in range(3):
            for j in range(3):
                self.entries[(row // 3) * 3 + i][(col // 3) * 3 + j].config(bg='lightgray')  
        for i in range(9):
            self.entries[i][col].config(bg='lightblue')  
            self.entries[row][i].config(bg='lightgray')

    def solve_sudoku(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
