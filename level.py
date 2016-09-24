from constants import *

class Level:
    # public Level()
    def __init__(self, maze, size,
                 name=None,
                 subname=None,
                 viewfield=2,
                 next_level_generator=None):
        # These attribute should not be modified during lifetime
        self.maze = maze
        self.size = size # [rows,cols]
        self.name = name or 'Untitled Level'
        self.subname = subname
        self.default_start = [0,0]
        self.default_viewfield = viewfield
        self.next_level = None
        self.next_level_generator = next_level_generator

        # Get player start point
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                if self.maze[row][col]== BLOCK_PLAYER:
                    self.default_start = [row, col]
                    self.maze[row][col]=0
                    break

        # Reset the level
        self.Reset()

    def __repr__(self):
        return '<Level({},@{}x{})>'.format(self.name,*self.size)

    def Reset(self):
        self.current = self.default_start
        self.gameover = False
        self.step = 0
        self.viewfield = self.default_viewfield
        self.overlay = {}

    def NextLevel(self):
        if self.next_level:
            return self.next_level

        if self.next_level_generator:
            self.next_level = self.next_level_generator()
            return self.next_level

        return None

    def GetBlock(self, row, col):
        '''Get the block code by 'row' and 'col'.'''

        if row == self.current[0] and col == self.current[1]:
            return BLOCK_PLAYER
        elif row<0 or col<0 or row>=self.size[0] or col>=self.size[1]:
            return BLOCK_BORDER
        else:
            if (row, col) in self.overlay.keys():
                return self.overlay[(row, col)]
            return self.maze[row][col]

    def __gen_row(self, row, scol, ecol):
        for col in range(scol, ecol):
            yield self.GetBlock(row, col)

    def View(self):
        '''Return the player view matrix.'''

        row, col = self.current
        offset = self.viewfield
        vf = self.viewfield * 2 + 1
        srow = row - offset
        scol = col - offset
        for r in range(srow, srow + vf):
            yield self.__gen_row(r, scol, scol + vf)

    def Maze(self):
        '''Return the full maze matrix.'''

        row, col = self.size
        for r in range(row):
            yield self.__gen_row(r, 0, col)

    def Move(self, direction):
        '''Move the current player position if possible.

        Returns:
            True if moved,
            False if being blocked.
        '''

        row, col = self.current
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
        if block in BLOCKING_BLOCKS:
            return False
        else:
            if block == BLOCK_EXIT:
                self.gameover = True
            elif block == BLOCK_VEIW_BUSTER:
                self.viewfield += 1
                self.overlay[(row, col)] = BLOCK_AIR
            self.current = [row,col]
            self.step += 1
            return True
