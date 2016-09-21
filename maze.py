import termcolor #for color
import os   #for clean
import msvcrt #for w,a,s,d
#-------------------------------------------
if os.name == 'nt': # If it's Windows OS
    os.system('chcp 65001') # Change encoding to UTF-8
#-------------------------------------------
Size=10  #10*10
Up=59432
Down=59440
Left=59435
Right=59437
Directions = [Up, Down, Left, Right]
#-------------------------------------------
prt_wall = lambda: termcolor.cprint('  ', 'white', 'on_green', end='')
prt_road = lambda: termcolor.cprint('  ', 'white', 'on_white', end='')
prt_door = lambda: termcolor.cprint('  ', 'white', 'on_red', end='')
prt_border = lambda: termcolor.cprint('  ', 'white', 'on_yellow', end='')
prt_player = lambda: termcolor.cprint('  ', 'white', 'on_blue', end='')
blocks = [prt_road, prt_wall, prt_door, prt_player, prt_border]
#--------------------------------------------------------------------
road=[
[3,0,1,1,1,1,1,1,0,1],
[1,0,0,0,0,0,0,0,0,1],
[0,0,1,0,1,1,0,1,0,0],
[0,1,1,0,0,0,0,1,0,1],
[0,0,0,0,1,1,0,0,0,1],
[1,0,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0],
[0,0,1,0,1,1,0,1,1,0],
[0,1,1,0,1,1,0,1,1,0],
[0,1,0,0,0,0,0,2,1,0]]
current=[0,0] # Coordinate
step=0 # How many steps you use in the game
for row in range(Size): # Set first site
    for column in range(Size):
        if road[row][column]==3:
            current=[row,column]
            road[row][column]=0
            break
#--------------------------------------------------------------------
def GetBlock(x, y):
    global current, road

    if x == current[0] and y == current[1]:
        return 3
    elif x<0 or y<0 or x>=Size or y>=Size:
        return 4
    else:
        return road[x][y]

def Show_Maze(start=None, end=None, zoom=1):
    start = start or [0,0]
    end = end or [Size-1,Size-1]
    for row in range(start[0],end[0]):
        for _ in range(zoom):
            for col in range(start[1], end[1]):
                for _ in range(zoom):
                    blocks[GetBlock(row,col)]()
            print()

def Move(direction):
    global current, step
    x = current[0]
    y = current[1]
    if direction==Up:
        x -= 1
    elif direction==Down:
        x += 1
    elif direction==Left:
        y -= 1
    elif direction==Right:
        y += 1
    else:
        return False

    block = GetBlock(x,y)
    if block == 4 or block == 1:
        return False
    else:
        current = [x,y]
        step += 1
        return True

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
    global current, step
    moved = True
    zoom = 2
    while True:
        if moved:
            clear()
            x,y = current
            print(' Step:',step,'Coordinare:', x,',',y)
            Show_Maze(start=[x-2,y-2],end=[x+3,y+3],zoom=zoom)
            print()

        moved = False
        code = get_unicode()

        if code == ord('q'):
            print('Bye Bye~~')
            return
        elif code == ord('c'):
            print('Fuck you bitch you cheat!')
            Show_Maze()
        elif code == ord('z'):
            zoom += 1
            if zoom >= 4:
                zoom = 1
            moved = True
        elif code in Directions:
            moved = Move(code)


#------------------------------------------------------------
if __name__ == '__main__':
    print("\nWelcome Raymond's Maze!! ")
    start()
