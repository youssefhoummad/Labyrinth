import tkinter as tk
from random import randint

from src.constants import *
from src.readmap import maze_from_file
from src.modules import Position, Item, Character


# ============ class =============
class Screen(tk.Canvas):
    """screen game: canvas"""
    def __init__(self, root, width=600, height=600):
        super().__init__(root, width=width, height=height)
        self.config(bd=0, highlightthickness=0, relief='ridge', bg='#685231')
        self.pack()
        self.focus_set()

    def draw_image(self, x, y, image, tags=None):
        x = x * WIDTH + WIDTH/2
        y = y * WIDTH + WIDTH/2
        self.create_image(x, y, image=image, tags=tags)

    def draw_maze(self, maze):
        keys_maze = {'#':BRICK, ' ':FLOOR}
        y = 0
        for line in maze:
            x = 0
            for char in line:
                self.draw_image(x, y, image=keys_maze.get(char, FLOOR), tags='maze')
                x += 1
            y += 1

    def draw_item(self, item):
        x, y = item.position.x, item.position.y
        self.draw_image(x, y, image=item.image, tags=item.tag)

    def erease(self,item):
        self.delete(item.tag)

    def erease_all(self):
        self.delete("all")

