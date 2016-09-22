import os
from termcolor import cprint, colored
from msvcrt import getch

from constants import *

logo = '''
     ____ ___  ___  ______    _______
    / __ `__ \/   |/___  /   / _____/.
   / / / / / / /| |   / /   / /___   .
  / / / / / / /_| |  / /   / ____/   .
 / / /_/ / / ___  | / /___/ /____    .
/_/     /_/_/   |_|/_____/______/    .
'''
def PrintLogo(width=100, padding=20):
    print()
    for l in logo.split('\n'):
        PaddingPrint(l, ('yellow',None), width, padding)
    print()

def Menu(items, width=100, padding=20, logo=True, Large=False):
    count = len(items)
    itemwidth = width - padding * 2
    current = 0
    while True:
        Clear()
        if logo:
            PrintLogo()
        for i in range(len(items)):
            if i == current:
                color = 'grey', 'on_white'
            else:
                color = None, None

            if Large:
                PaddingPrint(' '*itemwidth, color, width, padding)
            PaddingPrint(items[i], color, width, padding)
            if Large:
                PaddingPrint(' '*itemwidth, color, width, padding)

        PaddingPrint('─'*itemwidth, (None, None), width, padding)
        print()

        code = GetUnicode()
        if code == 13: # Enter
            return current
        elif code in KEY_TO_DIRECTION.keys():
            direction = KEY_TO_DIRECTION[code]
            if direction == UP:
                current -= 1
            elif direction == DOWN:
                current += 1
            if current < 0:
                current = count - 1
            elif current >= count:
                current = 0


def PaddingPrint(text, color, width, padding):
    itemwidth = width - padding * 2
    cprint(' '*padding, end='')
    cprint(Centerize(text,itemwidth), *color,end='')
    cprint(' '*padding)

def Centerize(text, width):
    lenght = len(text)
    spaces = width - lenght
    lspaces = int(spaces/2)
    rspaces = spaces - lspaces
    return ' '*lspaces + text + ' '*rspaces

def GetUnicode():
    code = 0
    while True:
        chcode = ord(getch())
        code *= 265
        code += chcode
        if chcode != 224:
            return code

def Clear():
    os.system('cls')
