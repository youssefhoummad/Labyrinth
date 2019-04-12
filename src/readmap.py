# ========== some func ================
def maze_from_file(map_file):
    "read map file and remove \\n; return  list of string"
    maze = []
    with open(map_file, 'r') as file:
        # remove char /n from end of string
        for line in file.readlines():
            maze.append(line[:-1])
    return maze
