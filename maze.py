from termcolor import cprint #for color
from level import Level
from constants import *
from printing import Menu, Centerize, GetUnicode, Clear
import os   #for clean
import msvcrt #for w,a,s,d
#-------------------------------------------
if os.name == 'nt': # If it's Windows OS
    os.system('chcp 65001') # Change encoding to UTF-8
#-------------------------------------------
prt_wall = lambda: cprint('  ', 'white', 'on_green', end='')
prt_road = lambda: cprint('  ', 'white', 'on_white', end='')
prt_door = lambda: cprint('  ', 'white', 'on_red', end='')
prt_border = lambda: cprint('  ', 'white', 'on_green', end='')
prt_player = lambda: cprint('  ', 'white', 'on_cyan', end='')
prt_buster = lambda: cprint('++', 'magenta', 'on_white', end='')
blocks = [prt_road, prt_wall, prt_door, prt_player, prt_buster, prt_border]
#--------------------------------------------------------------------
level = Level([
[3,0,1,1,1,1,1,1,0,1],
[1,0,0,0,0,0,0,0,0,1],
[0,0,1,0,1,1,0,1,0,0],
[0,1,1,0,0,0,0,1,0,1],
[0,0,0,0,1,1,0,0,0,1],
[1,0,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0],
[0,0,1,0,1,1,0,1,1,0],
[0,1,1,0,1,1,0,1,1,0],
[0,1,0,0,0,0,0,2,1,0]],
size=[10,10],viewfield=3)
#--------------------------------------------------------------------

def ShowMatrix(matrix, zoom=1):
    for row in matrix:
        cells = list(row)
        for _ in range(zoom):
            for cell in cells:
                for _ in range(zoom):
                    blocks[cell]()
            print()
            
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
    selected = Menu(['Start Game', 'Level Select', 'Exit'], Large=True)
    if selected == 0:
        game()
    elif selected == 1:
        pass
    else:
        return

def game():
    moved = True
    zoom = 2
    while True:
        if moved:
            Clear()
            ShowMatrix(level.View(), zoom)
            print(' Step:',level.step)
            print()
        if level.gameover:
            cprint('~~~~~~ Congratulations! ~~~~~~', 'yellow')
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
