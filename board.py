import tkinter as tk

class Board:
    def __init__(self, root, bg, side_length, side_pos, number_of_ships, size_of_board):
        self.canvas = tk.Canvas(root, bg=bg, width=side_length, height=side_length, highlightthickness=1, highlightbackground='black')
        self.canvas.pack(padx=50, side=side_pos)
        self.root = root
        self.side_length = side_length
        self.n = number_of_ships
        self.size = size_of_board
        self.cell_size = side_length // size_of_board
        self.draw_board()

    def draw_board(self):
        for i in range(self.size):
            self.canvas.create_line(self.cell_size * i, 0, self.cell_size * i, self.side_length)
            self.canvas.create_line(0, self.cell_size * i, self.side_length, self.cell_size * i)

    def create_rectangle(self, start, end, color=None, width=None):
        if color is None:
            self.canvas.create_rectangle(start[0], start[1], end[0], end[1], width=width)
        else:
            self.canvas.create_rectangle(start[0], start[1], end[0], end[1], fill=color)

    def clear_board(self):
        self.canvas.delete('all')
        for i in range(self.size):
            self.canvas.create_line(self.cell_size * i, 0, self.cell_size * i, self.side_length)
            self.canvas.create_line(0, self.cell_size * i, self.side_length, self.cell_size * i)

    def bind(self, event, function):
        self.canvas.bind(event, function)

    def create_cross(self, coordinates):
        x = coordinates[0] * 50
        y = coordinates[1] * 50
        self.canvas.create_line(x + 50, y, x, y + 50, fill='white', width=3)
        self.canvas.create_line(x, y, x + 50, y + 50, fill='white', width=3)

    def create_dot(self, coordinates):
        x = coordinates[0] * 50
        y = coordinates[1] * 50
        self.canvas.create_oval(x + 17, y + 17, x + 33, y + 33, fill='gray')