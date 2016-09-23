import os
from termcolor import cprint, colored
import colorama
from colorama import Fore, Back
from constants import *
colorama.init(autoreset=True)

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

if os.name == 'nt':
    import ctypes
    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int), ("visible", ctypes.c_byte)]

cm = lambda t: colored(t, 'magenta')
cy = lambda t: colored(t, 'yellow')
cc = lambda t: colored(t, 'cyan')
cg = lambda t: colored(t, 'green')

logo = \
Fore.YELLOW+'     ____ ___  ___ '+Fore.GREEN+' ______'+Fore.CYAN+'    _______ \n' + \
Fore.YELLOW+'    / __ `__ \/   |'+Fore.GREEN+'/___  /'+Fore.CYAN+'   / _____/ \n' + \
Fore.YELLOW+'   / / / / / / /| |'+Fore.GREEN+'   / / '+Fore.CYAN+'  / /___    \n' + \
Fore.YELLOW+'  / / / / / / /_| |'+Fore.GREEN+'  / /  '+Fore.CYAN+' / ____/    \n' + \
Fore.YELLOW+' / / /_/ / / ___  |'+Fore.GREEN+' / /___'+Fore.CYAN+'/ /____     \n' + \
Fore.YELLOW+'/_/     /_/_/   |_|'+Fore.GREEN+'/_____/'+Fore.CYAN+'______/   '+Fore.MAGENTA+'ヽ(✿ﾟ▽ﾟ)ノ'

def PrintLogo():
    length = 45
    print()
    for l in logo.split('\n'):
        cl = Centerize(l, length=length)
        PaddingPrint(cl, centerize=False)
    print()
    print()

def HideCursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

def ShowCursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

def ResetCursor(r=1,c=1):
    print("\033[%d;%dH" % (r, c), end='')

def Menu(items, title=None, logo=True, Large=False):
    Clear()
    count = len(items)
    current = 0
    while True:
        #Clear()
        ResetCursor()
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
