import os   #for clean
#-------------------------------------------
if os.name == 'nt': # If it's Windows OS
    os.system('chcp 65001') # Change encoding to UTF-8

import msvcrt #for w,a,s,d
import random
from datetime import date
from termcolor import cprint, colored #for color

from level import Level
from generator import MazeGenerator
from constants import *
from loader import GetLevels, LoadLevel
from printing import Menu, Centerize, GetUnicode, Clear, PaddingPrint

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
    '002'
]
level = None
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

def introduce():
    Clear()

    print('──────────────────────────')
    print('**Keyword**\n   h : help\n   q : quit')
    print('──────────────────────────\n')
    print('**How to Play**')
    print('   Use arrow key to move !!!\n')
    print('──────────────────────────\n')
    print('Press Enter To Continue~~~')

def help():
    introduce()

def start():
    #introduce()
    selected = Menu(['Start Game', 'Daliy Run', 'Random Level', 'Level Select', 'Exit'], Large=True)
    if selected == 0:
        game()
    elif selected == 1:
        daliy_run()
    elif selected == 2:
        random_level()
    elif selected == 3:
        level_select()
    else:
        return

def random_level():
    global level
    mg = MazeGenerator()
    level = mg.to_level()
    game()

def level_select():
    global level
    levels = GetLevels()
    levelnames = [os.path.basename(x) for x in levels]
    selected = Menu(levelnames+['< Back'], title="Select a Level", Large=True)
    if selected in [len(levelnames),-1]:
        # Back
        start()
    else:
        level = LoadLevel(levels[selected])
        game()

def daliy_run():
    global level
    seed = date.today().strftime('%Y%m%d')
    mg = MazeGenerator(seed=seed+'MAZEPY')
    level = mg.to_level()
    level.name = 'Daliy Run ({})'.format(seed)
    game()

def game():
    global level
    if not level:
        level = LoadLevel(random.choice(levelpaths))
    moved = True
    zoom = 2
    while True:
        if moved:
            Clear()
            print()
            PaddingPrint(level.name, 'cyan')
            print()
            ShowMatrix(level.View(), zoom)
            print()
            PaddingPrint('Step:'+str(level.step))
            print()
        if level.gameover:
            PaddingPrint('~~~~~~ Congratulations! ~~~~~~', 'yellow')
            print()
            return

        moved = False
        code = GetUnicode()

        if code == ord('q'):
            print('Bye Bye~~')
            return
        elif code == ord('c'):
            cprint('Fuck you bitch you cheat!', 'red')
            ShowMatrix(level.Maze())
        elif code == ord('z'):
            zoom += 1
            if zoom >= 4:
                zoom = 1
            moved = True
        elif code in KEY_TO_DIRECTION.keys():
            moved = level.Move(KEY_TO_DIRECTION[code])


#------------------------------------------------------------
if __name__ == '__main__':
    print("\nWelcome Raymond's Maze!! ")
    start()
