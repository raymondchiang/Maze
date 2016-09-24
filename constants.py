from colorama import Fore  as CF
from colorama import Back  as CB
from colorama import Style as CS

#CF: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#CB: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#CS: DIM, NORMAL, BRIGHT, RESET_ALL

UP=0
DOWN=1
LEFT=2
RIGHT=3
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
KEY_TO_DIRECTION = {
    # Arrow Keys
    59432: UP,
    59440: DOWN,
    59435: LEFT,
    59437: RIGHT,
    # wasd
    119: UP,
    115: DOWN,
    97: LEFT,
    100: RIGHT,
    # WASD
    87: UP,
    83: DOWN,
    65: LEFT,
    68: RIGHT
}

BLOCK_AIR = 0
BLOCK_WALL = 1
BLOCK_EXIT = 2
BLOCK_PLAYER = 3
BLOCK_VEIW_BUSTER = 4
BLOCK_BORDER = -1
BLOCK_KEY = 100
BLOCK_GATE = 200
BLOCK_PORTAL = 300

BLOCKS_KEYS = (100, 199)
BLOCKS_GATES = (200, 299)
BLOCKS_PORTALS = (300, 399)

BLOCKING_BLOCKS = [BLOCK_WALL, BLOCK_BORDER, BLOCK_GATE]

LOADER_SYMBOLS = {
    ' ': BLOCK_AIR,
    '$': BLOCK_WALL,
    'P': BLOCK_PLAYER,
    'E': BLOCK_EXIT,
    'K': BLOCK_KEY,
    'G': BLOCK_GATE,
    'T': BLOCK_PORTAL,
    '+': BLOCK_VEIW_BUSTER
}

SCREEN_WIDTH = 100
SCREEN_PADDING = 10
SCREEN_ITEM_WIDTH = SCREEN_WIDTH - SCREEN_PADDING * 2

CHEAT_PEEK_TIMER = 0.5

LOGO_FIGLET_LENGTH = 42
LOGO_FIGLET = '\n' + \
CF.RED+'     ____ ___ '+CF.YELLOW +' ___ '+CF.GREEN+' ______'+CF.CYAN+'    ______ \n' + \
CF.RED+'    / __ `__ \\'+CF.YELLOW+'/   |'+CF.GREEN+'/___  /'+CF.CYAN+'   / ____/ \n' + \
CF.RED+'   / / / / / /'+CF.YELLOW +' /| |'+CF.GREEN+'   / / '+CF.CYAN+'  / /___   \n' + \
CF.RED+'  / / / / / '+CF.YELLOW +'/ /_| |'+CF.GREEN+'  / /  '+CF.CYAN+' / ____/   \n' + \
CF.RED+' / / /_/ / /'+CF.YELLOW +' ___  |'+CF.GREEN+' / /___'+CF.CYAN+'/ /____    \n' + \
CF.RED+'/_/     /_'+CF.YELLOW +'/_/   |_|'+CF.GREEN+'/_____'+CF.CYAN+'/______/  '+CF.MAGENTA+'ヽ(✿ﾟ▽ﾟ)ノ\n\n' + \
CF.WHITE+' '*23+' by Raymond & Anthony.'
