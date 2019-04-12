import tkinter as tk



# ========== constants ==============
ROOT = tk.Tk()
ROOT.title("Macgryvers Labyrinth")
ROOT.resizable(0, 0) # disable resizing

BRICK = tk.PhotoImage(file='src/images/brick.png')
ETHER = tk.PhotoImage(file='src/images/ether.png')
GURDIAN = tk.PhotoImage(file='src/images/guardian.png')
MAC_GYVER = tk.PhotoImage(file='src/images/mac_gyver.png')
NEEDLE = tk.PhotoImage(file='src/images/needle.png')
TUBE = tk.PhotoImage(file='src/images/tube.png')
FLOOR = tk.PhotoImage(file='src/images/floor.png')

WIN = tk.PhotoImage(file='src/images/win.png')
LOSE = tk.PhotoImage(file='src/images/lose.png')
REPLAY = tk.PhotoImage(file='src/images/replay.png')

WIDTH = 40 # pixels