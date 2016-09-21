class Level:
    # public Level()
    def __init__(self, maze, size):
        self.maze = maze # 馬子 ヽ(✿ﾟ▽ﾟ)ノ
        self.size = size # [x,y]
        self.current = [0,0]
        self.step = 0

    def get_block(self, x, y):
        if x == self.current[0] and y == self.current[1]:
            return 3
        elif x<0 or y<0 or x>=self.size[0] or y>=self.size[1]:
            return 4
        else:
            return self.maze[x][y]

    def move(self, direction):
        pass
