#----------- Unicode Hack --------------------------------
import os   #for clean
import sys
if os.name == 'nt': # If it's Windows OS
    os.system('chcp 65001') # Change encoding to UTF-8
    #sys.stdout.encoding = 'cp65001'
#----------- Built-in Packages -------------------------------
import msvcrt #for w,a,s,d
import random
from datetime import date
from termcolor import cprint, colored #for color
#----------- Custom Packages -------------------------------------------
from level import Level
from generator import MazeGenerator
from constants import *
from loader import GetLevels, LoadLevel
from printing import Menu, Centerize, GetUnicode, Clear, PaddingPrint, HideCursor, ShowCursor, ResetCursor, PrintFiglet
#-------------------------------------------
prt_wall = lambda: colored('  ', 'white', 'on_green')
prt_road = lambda: colored('  ', 'white', 'on_white')
prt_door = lambda: colored('  ', 'white', 'on_red')
prt_border = lambda: colored('  ', 'white', 'on_green')
prt_player = lambda: colored('  ', 'white', 'on_cyan')
prt_buster = lambda: colored('++', 'magenta', 'on_white')
blocks = [prt_road, prt_wall, prt_door, prt_player, prt_buster, prt_border]
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
                line+=blocks[cell]()
                length+=2
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
        moved = True
        self.zoom = 2
        while True:
            if moved:
                self.FrameUpdate()
            if self.level.gameover:
                PaddingPrint('~~~~~~ Congratulations! ~~~~~~', 'yellow')
                print()
                return

            moved = False
            code = GetUnicode()

            if code in [27, ord('q'), ord('Q')]:
                Esc = Menu(['Continue','Back to Menu','Exit'], header=lambda: PrintFiglet('Pause'), Large=True)
                #pause_menu():
                if Esc==0 or Esc==-1:
                    moved = True
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
                moved = True
                Clear()
            elif code in KEY_TO_DIRECTION.keys():
                moved = self.level.Move(KEY_TO_DIRECTION[code])


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
        seed = date.today().strftime('%Y%m%d')
        mg = MazeGenerator(seed=seed+'MAZEPY')
        self.level = mg.to_level()
        self.level.name = 'Daliy Run ({})'.format(seed)
        self.Play()

    def FrameUpdate(self):
        #Clear()
        ResetCursor()
        print()
        PaddingPrint(self.level.name, 'cyan')
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
