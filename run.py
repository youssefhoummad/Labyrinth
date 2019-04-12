import tkinter as tk
from random import randint, choice
from os import listdir

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

class Game:
    """main class for Macgyver's Labyrinth"""
    def __init__(self, screen, maze):
        self.screen = screen
        self.maze = maze
        self.initialize()
        self.handle_key()

        self.items_collected = 0
        self.game_over = False

    def initialize(self):
        "initialize the game"
        pos_macgryver = self.find_position_from_maze('@')
        self.macgryver = Character(pos_macgryver, MAC_GYVER, 'macgryver')

        pos_guardian = self.find_position_from_maze('.')
        self.guardian = Character(pos_guardian, GURDIAN, 'guardian')

        items_positions = self.random_position_item()
        items_tags = ('ether', 'needle', 'tube')
        items_images = (ETHER, NEEDLE, TUBE)

        self.items = [Item(items_positions[i], items_images[i], items_tags[i]) for i in range(3)]

        self.draw_on_screen()

    def draw_on_screen(self):
        "draw all item and character and maze on screen"
        self.screen.draw_maze(self.maze)

        for item in self.items:
            self.screen.draw_item(item)

        self.screen.draw_item(self.macgryver)
        self.screen.draw_item(self.guardian)

    def random_position_item(self):
        "random ' ' from maze"
        random_pos = []
        x, y = 0, 0
        for i in range(3):
            char = ''
            # be sure the random position not in brick
            while char != ' ':
                x, y = randint(1, 13), randint(1, 13)
                char = self.maze[y][x]
            random_pos.append((x, y))
        return [Position(x, y) for (x, y) in random_pos]           

    def find_position_from_maze(self, char):
        "find the position for char in maze"
        x, y = 0, 0
        for row in self.maze:
            if char in row:
                x = row.find(char)
                break
            y += 1
        return Position(x, y)

    def legal_move(self, new_position):
        if self.game_over:
            return False
        j = new_position.x
        i = new_position.y
        if j == 15:
            return False
        return self.maze[i][j] in ' @.'

    def move_macgyver(self, dir_x, dir_y):
        dir_position = Position(dir_x, dir_y)
        new_position = self.macgryver.position + dir_position
        if self.legal_move(new_position):
            self.macgryver.position = new_position
            self.screen.erease(self.macgryver)
            self.screen.draw_item(self.macgryver)
            self.check_game()
        return None

    def handle_key(self):
        self.screen.bind('<Left>', lambda event, x=-1, y=0: self.move_macgyver(x, y))
        self.screen.bind('<Right>', lambda event, x=1, y=0: self.move_macgyver(x, y))
        self.screen.bind('<Up>', lambda event, x=0, y=-1: self.move_macgyver(x, y))
        self.screen.bind('<Down>', lambda event, x=0, y=1: self.move_macgyver(x, y))

        self.screen.bind('<F1>', lambda event: self.play_again())

    def check_game(self):
        "check macgryver is catched or is win"
        for item in self.items:
            if item.position == self.macgryver.position:
                self.items_collected += 1
                self.screen.erease(item)
                self.items.remove(item)
        if self.macgryver.position == self.guardian.position:
            self.game_over = True

            if self.items_collected == 3:
                self.winer()
            else:
                self.loser()

    def winer(self):
        "win..."
        self.screen.draw_image(7, 6, WIN)
        self.screen.draw_image(7, 8, REPLAY)

    def loser(self):
        "lose..."
        self.screen.draw_image(7, 6, LOSE)
        self.screen.draw_image(7, 8, REPLAY)

    def play_again(self):
        "play game again"
        self.items_collected = 0
        self.game_over = False
        self.screen.erease_all()
        self.initialize()

# ============== MAIN PROGRAM =============
if __name__ == '__main__':
    map = choice(listdir('src/maps'))
    maze_map = maze_from_file('src/maps/' + map)
    screen = Screen(ROOT)
    game = Game(screen, maze_map)
    ROOT.mainloop()
