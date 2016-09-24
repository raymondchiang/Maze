if __name__ == '__main__':
    print('Initialization...')
#----------- Built-in Packages -------------------------------
import os
import sys
import random
from datetime import date
from termcolor import cprint, colored #for color
#----------- Custom Packages -------------------------------------------
from printing import (
    Menu, Centerize, GetUnicode,
    Clear, PaddingPrint, HideCursor,
    ShowCursor, ResetCursor,
    PrintFiglet)
from level import Level
from generator import MazeGenerator
from constants import *
from loader import GetLevels, LoadLevel
#-------------------------------------------
PRINT_BLOCKS = {
    BLOCK_AIR         : CB.WHITE + '  ',
    BLOCK_WALL        : CB.GREEN + '  ',
    BLOCK_EXIT        : CB.RED   + '  ',
    BLOCK_PLAYER      : CB.CYAN  + '  ',
    BLOCK_BORDER      : CB.GREEN + '  ',
    BLOCK_KEY         : CB.WHITE + CF.YELLOW + ' ⚷',
    BLOCK_GATE        : CB.YELLOW + CF.RED + 'XX',
    BLOCK_PORTAL      : CB.BLUE + '*>',
    BLOCK_VEIW_BUSTER : CB.WHITE + CF.MAGENTA + ' +'
}
#--------------------------------------------------------------------
levelpaths = [
    '001',
    '002',
    '003'
]
#--------------------------------------------------------------------

def ShowMatrix(matrix, zoom=1):
    for row in matrix:
        line = ''
        length = 0
        for cell in row:
            for _ in range(zoom):
                line+=PRINT_BLOCKS[cell]
                length+=2
        line += CS.RESET_ALL
        line = Centerize(line, length=length)
        for _ in range(zoom):
            PaddingPrint(line, centerize=False)

class Game:
    def __init__(self):
        self.level = None
        self.zoom  = 2

    def MainMenu(self):
        selected = Menu(['Start Game', 'Daliy Run', 'Random Level', 'Level Select', 'Exit'], Large=True)
        if selected == 0:
            self.Play()
        elif selected == 1:
            self.DaliyRun()
        elif selected == 2:
            self.RandomLevel()
        elif selected == 3:
            self.LevelSelect()
        else:
            self.Exit()

    def Exit(self):
        Clear()
        sys.exit()

    def Play(self):
        Clear()
        if not self.level:
            self.level = LoadLevel(levelpaths[0])
        update_needed = True
        self.zoom = 2
        while True:
            if update_needed:
                self.FrameUpdate()
            if self.level.gameover:
                PaddingPrint('~~~~~~ Congratulations! ~~~~~~', 'yellow')
                print()
                return

            update_needed = False
            code = GetUnicode()

            if code in [27, ord('q'), ord('Q')]:
                Esc = Menu(['Continue','Back to Menu','Exit'], header=lambda: PrintFiglet('Pause'), Large=True)
                #pause_menu():
                if Esc==0 or Esc==-1:
                    update_needed = True
                    Clear()
                elif Esc==1:
                    self.MainMenu()
                elif Esc==2:
                    self.Exit()

            elif code == ord('c'):
                cprint('Fuck you bitch you cheat!', 'red')
                ShowMatrix(self.level.Maze())
            elif code == ord('z'):
                self.zoom += 1
                if self.zoom >= 4:
                    self.zoom = 1
                update_needed = True
                Clear()
            elif code in KEY_TO_DIRECTION.keys():
                update_needed = self.level.Move(KEY_TO_DIRECTION[code])


    def help(self):
        pass

    def RandomLevel(self):
        mg = MazeGenerator()
        self.level = mg.to_level()
        self.Play()

    def LevelSelect(self):
        levels = GetLevels()
        levelnames = [os.path.basename(x) for x in levels]
        selected = Menu(levelnames+['< Back'], header=lambda: PrintFiglet('Select a Level'), Large=True)
        if selected in [len(levelnames),-1]:
            # Back
            self.MainMenu()
        else:
            self.level = LoadLevel(levels[selected])
            self.Play()

    def DaliyRun(self):
        today = date.today().strftime('%Y-%m-%d')
        mg = MazeGenerator(seed=today+'MAZEPY')
        self.level = mg.to_level()
        self.level.name = 'Daliy  Run'
        self.level.subname = today
        self.Play()

    def FrameUpdate(self):
        #Clear()
        ResetCursor()
        print()
        PaddingPrint(self.level.name)
        if self.level.subname:
            PaddingPrint(self.level.subname, 'cyan')
        print()
        ShowMatrix(self.level.View(), self.zoom)
        print()
        PaddingPrint('Step:'+str(self.level.step))
        print()

#------------------------------------------------------------
if __name__ == '__main__':
    HideCursor()
    Clear()
    g = Game()
    g.MainMenu()
    ShowCursor()
    Clear()
