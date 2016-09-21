from constants import *

class Level:
    # public Level()
    def __init__(self, maze, size):
        self.maze = maze # 馬子 ヽ(✿ﾟ▽ﾟ)ノ
        self.size = size # [row,col]
        self.current = [0,0]
        self.step = 0
        self.gameover = False

        for row in range(self.size[1]):
            for col in range(self.size[0]):
                if self.maze[row][col]==3:
                    self.current=[row,col]
                    self.maze[row][col]=0
                    break

    def GetBlock(self, row, col):
        if row == self.current[0] and col == self.current[1]:
            return 3
        elif row<0 or col<0 or row>=self.size[0] or col>=self.size[1]:
            return 4
        else:
            return self.maze[row][col]

    def Move(self, direction):
        row = self.current[0]
        col = self.current[1]
        if direction==UP:
            row -= 1
        elif direction==DOWN:
            row += 1
        elif direction==LEFT:
            col -= 1
        elif direction==RIGHT:
            col += 1
        else:
            return False

        block = self.GetBlock(row,col)
        if block == 4 or block == 1:
            return False
        else:
            if block == 2:
                self.gameover = True
            self.current = [row,col]
            self.step += 1
            return True