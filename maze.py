import termcolor #for color
import os   #for clean
import msvcrt #for w,a,s,d
#-------------------------------------------
if os.name == 'nt': # If it's Windows OS
    os.system('chcp 65001') # Change encoding to UTF-8
#-------------------------------------------
Size=10  #10*10
Up=72
Down=80
Left=75
Right=77
#-------------------------------------------
prt_wall = lambda: termcolor.cprint('  ', 'white', 'on_green', end='')
prt_road = lambda: termcolor.cprint('  ', 'white', 'on_white', end='')
prt_door = lambda: termcolor.cprint('  ', 'white', 'on_red', end='')
prt_border = lambda: termcolor.cprint('  ', 'white', 'on_yellow', end='')
prt_player = lambda: termcolor.cprint('  ', 'white', 'on_blue', end='')
blocks = [prt_road, prt_wall, prt_door,prt_player]
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
[0,1,0,0,0,0,0,0,1,2]]
current=[0,0] # Coordinate
for row in range(Size): # Set first site
    for column in range(Size):
        if road[row][column]==3:
            current=[row,column]
#--------------------------------------------------------------------
def Global_Map(road):
    for row in range(len(road)):
        for column in range(len(road)):
            blocks[road[row][column]]()
        print()
    print()
def Show_Maze(current,road,step,zoom=1):
    print('─────────')
    print(current)
    x = current[0]-2
    y = current[1]-2
    print(x,y)
    for row in range(x, x+5):
        for _ in range(zoom):
            for col in range(y, y+5):
                for _ in range(zoom):
                    if col<0 or row<0 or row>Size-1 or col>Size-1:
                        prt_border()
                    else:
                        if road[row][col]==2:
                            prt_door()
                        elif road[row][col]==1:
                            prt_wall()
                        elif road[row][col]==0:
                            prt_road()
                        else:
                            prt_player()
            print()
    print('─────────\nStep',step[0])
def Move(road,current,loc,step):
    if ord(loc)==Up:
        if current[0]==0 or road[current[0]-1][current[1]]==1:
            return True
        else:
            road[current[0]-1][current[1]],road[current[0]][current[1]]=road[current[0]][current[1]],road[current[0]-1][current[1]]
            current[0]-=1
            step[0]+=1
    elif ord(loc)==Left:
        if current[1]==0 or road[current[0]][current[1]-1]==1:
            return True
        else:
            road[current[0]][current[1]-1],road[current[0]][current[1]]=road[current[0]][current[1]],road[current[0]][current[1]-1]
            current[1]-=1
            step[0]+=1
    elif ord(loc)==Down:
        if current[0]==9 or road[current[0]+1][current[1]]==1:
            return True
        else:
            road[current[0]+1][current[1]],road[current[0]][current[1]]=road[current[0]][current[1]],road[current[0]+1][current[1]]
            current[0]+=1
            step[0]+=1
    elif ord(loc)==Right:
        if current[1]==9 or road[current[0]][current[1]+1]==1:
            return True
        else:
            road[current[0]][current[1]+1],road[current[0]][current[1]]=road[current[0]][current[1]],road[current[0]][current[1]+1]
            current[1]+=1
            step[0]+=1
def introduce():
    print('──────────────────────────')
    print('**Keyword**\n   h : help\n   q : quit\n   c : cheat')
    print('──────────────────────────\n')
    print('**How to Play**')
    print('   Use arrow key to move !!!\n')
    print('──────────────────────────\n')
    print('Press Anywhere To Continue~~~')
    msvcrt.getch()
#------------------------------------------------------------
cheat=False
need_help=False
step=[0,] # How many steps you use in the game
is_clean=True
print("\nWelcome Raymond's Maze!! ")
introduce()
while True:
    if is_clean:
        is_clean=False
    else:
        os.system('cls') # Refresh screen
        Show_Maze(current,road,step,3)
    if cheat==True:
        cheat=False
        Global_Map(road)
        print('Coordinare :',current,end=' \n\n')
    if need_help==True:
        need_help=False
        introduce()
    Keyword = msvcrt.getch()
    if ord(Keyword)==99:#c-->cheat
        cheat=True
        continue
    if ord(Keyword)==113:#q-->quit
        print('Bye Bye~~')
        break
    if ord(Keyword)==104:#h-->help
        need_help=True
        continue
    loc = msvcrt.getch()
    is_clean=Move(road,current,loc,step)
    if current==[Size,Size]:
        print('Congratulations !! ')
        break
