from constants import *

class Level:
    # public Level()
    def __init__(self, maze, size):
        self.maze = maze # 馬子 ヽ(✿ﾟ▽ﾟ)ノ
        self.size = size # [x,y]
        self.current = [0,0]
        self.step = 0
        self.gameover = False

    def GetBlock(self, x, y):
        if x == self.current[0] and y == self.current[1]:
            return 3
        elif x<0 or y<0 or x>=self.size[0] or y>=self.size[1]:
            return 4
        else:
            return self.maze[x][y]

    def Move(self, direction):
        x = self.current[0]
        y = self.current[1]
        if direction==UP:
            x -= 1
        elif direction==DOWN:
            x += 1
        elif direction==LEFT:
            y -= 1
        elif direction==RIGHT:
            y += 1
        else:
            return False

        block = self.GetBlock(x,y)
        if block == 4 or block == 1:
            return False
        else:
            if block == 2:
                self.gameover = True
            self.current = [x,y]
            self.step += 1
            return True