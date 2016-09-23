import os
from termcolor import cprint, colored

from constants import *

try:
    from msvcrt import getch
except ImportError:
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

cm = lambda t: colored(t, 'magenta')
cy = lambda t: colored(t, 'yellow')
cc = lambda t: colored(t, 'cyan')
cg = lambda t: colored(t, 'green')

logo = \
cy('     ____ ___  ___ ')+cg(' ______')+cc('    _______ \n') + \
cy('    / __ `__ \/   |')+cg('/___  /')+cc('   / _____/ \n') + \
cy('   / / / / / / /| |')+cg('   / / ')+cc('  / /___    \n') + \
cy('  / / / / / / /_| |')+cg('  / /  ')+cc(' / ____/    \n') + \
cy(' / / /_/ / / ___  |')+cg(' / /___')+cc('/ /____     \n') + \
cy('/_/     /_/_/   |_|')+cg('/_____/')+cc('______/   ') + cm('ヽ(✿ﾟ▽ﾟ)ノ') + '\n'

def PrintLogo():
    length = 45
    print()
    for l in logo.split('\n'):
        cl = Centerize(l, length=length)
        PaddingPrint(cl, centerize=False)
    print()

def Menu(items, title=None, logo=True, Large=False):
    count = len(items)
    current = 0
    while True:
        Clear()
        if logo:
            PrintLogo()

        if title:
            PaddingPrint(title, 'cyan', attrs=['bold'])
            print()

        for i in range(len(items)):
            if i == current:
                color = 'grey', 'on_white'
            else:
                color = None, None

            if Large:
                PaddingPrint(' '*SCREEN_ITEM_WIDTH, *color)
            PaddingPrint(items[i], *color)
            if Large:
                PaddingPrint(' '*SCREEN_ITEM_WIDTH, *color)

        PaddingPrint('─'*SCREEN_ITEM_WIDTH)
        print()

        code = GetUnicode()
        if code == 13: # Enter
            return current
        elif code == 27: # Escape
            return -1
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


def PaddingPrint(text, *args, centerize=True, **kw):
    cprint(' '*SCREEN_PADDING, end='')
    text = text if not centerize else Centerize(text,SCREEN_ITEM_WIDTH)
    cprint(text, *args, **kw ,end='')
    cprint(' '*SCREEN_PADDING)

def Centerize(text, width=SCREEN_ITEM_WIDTH, length=None):
    if length is None:
        length = len(text)
    spaces = width - length
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
