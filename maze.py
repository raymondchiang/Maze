from termcolor import cprint #for color
from level import Level
from constants import *
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
blocks = [prt_road, prt_wall, prt_door, prt_player, prt_border]
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
size=[10,10])
#--------------------------------------------------------------------

def Show_Maze(start=None, end=None, zoom=1):
    start = start or [0,0]
    end = end or level.size
    for row in range(start[0],end[0]):
        for _ in range(zoom):
            for col in range(start[1], end[1]):
                for _ in range(zoom):
                    blocks[level.GetBlock(row,col)]()
            print()

def get_unicode():
    code = 0
    while True:
        chcode = ord(msvcrt.getch())
        code *= 265
        code += chcode
        if chcode != 224:
            return code

def clear():
    os.system('cls')

def introduce():
    clear()
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
    introduce()
    key = input()
    if key == 'q':
        return
    game()


def game():
    moved = True
    zoom = 2
    while True:
        if moved:
            clear()
            x,y = level.current
            print(' Step:',level.step,' Coordinare:', x,',',y)
            Show_Maze(start=[x-2,y-2],end=[x+3,y+3],zoom=zoom)
            print()
        if level.gameover:
            cprint('~~~~~~ Congratulations! ~~~~~~', 'yellow')
            return

        moved = False
        code = get_unicode()

        if code == ord('q'):
            print('Bye Bye~~')
            return
        elif code == ord('c'):
            cprint('Fuck you bitch you cheat!', 'red')
            Show_Maze()
        elif code == ord('z'):
            zoom += 1
            if zoom >= 4:
                zoom = 1
            moved = True
        elif code in DIRECTIONS:
            moved = level.Move(code)


#------------------------------------------------------------
if __name__ == '__main__':
    print("\nWelcome Raymond's Maze!! ")
    game()

