import os
from termcolor import cprint, colored
import colorama
from colorama import Fore, Back
from constants import *
colorama.init(autoreset=True)
from pyfiglet import Figlet

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


logo = \
Fore.RED+'     ____ ___ '+Fore.YELLOW +' ___ '+Fore.GREEN+' ______'+Fore.CYAN+'    ______ \n' + \
Fore.RED+'    / __ `__ \\'+Fore.YELLOW+'/   |'+Fore.GREEN+'/___  /'+Fore.CYAN+'   / ____/ \n' + \
Fore.RED+'   / / / / / /'+Fore.YELLOW +' /| |'+Fore.GREEN+'   / / '+Fore.CYAN+'  / /___    \n' + \
Fore.RED+'  / / / / / '+Fore.YELLOW +'/ /_| |'+Fore.GREEN+'  / /  '+Fore.CYAN+' / ____/    \n' + \
Fore.RED+' / / /_/ / /'+Fore.YELLOW +' ___  |'+Fore.GREEN+' / /___'+Fore.CYAN+'/ /____     \n' + \
Fore.RED+'/_/     /_'+Fore.YELLOW +'/_/   |_|'+Fore.GREEN+'/_____'+Fore.CYAN+'/______/  '+Fore.MAGENTA+'ヽ(✿ﾟ▽ﾟ)ノ\n\n' + \
Fore.WHITE+' '*23+' by Raymond & Anthony.'

def PrintLogo():
    length = 42
    print()
    for l in logo.split('\n'):
        cl = Centerize(l, length=length)
        PaddingPrint(cl, centerize=False)

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

def PrintFiglet(text, font='slant', color='cyan'):
    figlet = Figlet(font=font)
    text = figlet.renderText(text).rstrip()
    max_length = 0
    for s in text.split('\n'):
        length = len(s)
        if length > max_length:
            max_length = length

    print()
    for l in text.split('\n'):
        cl = Centerize(l, length=max_length)
        PaddingPrint(cl, centerize=False, color=color)

def Menu(items, title=None, header=None, Large=False):
    Clear()
    count = len(items)
    current = 0
    header = header or PrintLogo
    while True:
        ResetCursor()
        header()
        print()
        if title:
            PaddingPrint(title, 'cyan', attrs=['bold'])

        PaddingPrint('─'*SCREEN_ITEM_WIDTH)

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
