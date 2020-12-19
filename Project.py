from PIL import Image
from PIL import ImageDraw
from PIL import Image, ImageColor
from PIL import ImageDraw
from math import pi, sin, cos
from tkinter import *
tk=Tk()
canvas= Canvas(tk, width=500,height=500)
canvas.pack()
height = 300
width = 400
left_x = int(width * -0.5)
right_x = int(width * 1.5)
top_y = int(height * -0.5)
bottom_y = int(height * 1.5)
resolution = int(width * 0.01)
num_columns = (right_x - left_x) / resolution
num_rows = (bottom_y - top_y) / resolution
grid = [[0 for _ in range (int(num_rows))] for _ in range(int(num_columns))]
default_angle = pi * 0.25
for column in range (int(num_columns)):
    for row in range(int(num_rows)):
        grid[column][row] = default_angle



x = 500
y = 100


for n in [0..num_steps]) :
    draw_vertex(x, y)
    x_offset = x - left_x
    y_offset = y - top_y
    column_index = int(x_offset / resolution)
    row_index = int(y_offset / resolution)
    grid_angle = grid[column_index][row_index]
    x_step = step_length * cos(grid_angle)
    y_step = step_length * sin(grid_angle)
    x = x + x_step
    y = y + y_step
