import argparse
from tkinter import *

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board


def __init__(self, sudoku):
    self.canvas = Canvas(width=WIDTH, height=HEIGHT)
    self.game = sudoku
    self.canvas.pack(fill=BOTH, side=TOP)
    self.draw_grid()
    self.draw_puzzle()

def __draw_grid():
    for i in range(1,10):
        color = "black" if i % 3 == 0 else "gray"

        x0 = MARGIN + i * SIDE
        y0 = MARGIN
        x1 = MARGIN + i * SIDE
        y1 = HEIGHT - MARGIN
        self.canvas.create_line(x0, y0, x1, y1, fill=color)

        x0 = MARGIN
        y0 = MARGIN + i * SIDE
        x1 = WIDTH - MARGIN
        y1 = MARGIN + i * SIDE
        self.canvas.create_line(x0, y0, x1, y1, fill=color)

def __draw_puzzle():
    for i in range(0,9):
        for j in range(0,9):
            print(i,j)
            answer = sudoku[i][j]
            if answer != 0:
                x = MARGIN + j * SIDE + SIDE / 2
                y = MARGIN + i * SIDE + SIDE / 2
                original = game.start_puzzle[i][j]
                color = "black"
                self.canvas.create_text(
                    x, y, text=answer, tags="numbers", fill=color
                )
