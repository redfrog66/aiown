import pygame
import numpy as np
from tqdm import tqdm

# SZÍNEK
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Jelek a játék dekódolásához

# - üres (egy labdához vagy játékoshoz nem tartozó cella)
SIGN_EMPTY = " "
# labda
SIGN_BALL = "o"
# játékos (a téglalap)
SIGN_PLAYER = "x"

# az "ablak" nagyítás nélküli mérete
SPACE_SIZE = (20,20)

# Ezt a felhasználói felület ablakának felnagyítására fogjuk használni
# A felhasználói felület ablakának mérete SPACE_SIZE * ZOOM_SIZE
ZOOM_SIZE = 10

# 3 műveletünk van, amelyet az ügynök bármikor megtehet:

# üresjárat (nem változik a helyzet)
ACTION_IDLE = "IDLE"

ACTION_LEFT = "LEFT"

ACTION_RIGHT = "RIGHT"

ACTIONS = [
    ACTION_IDLE,
    ACTION_LEFT,
    ACTION_RIGHT
]

# A lapát kezdő koordinátái
rect_x = SPACE_SIZE[0] // 2
rect_y = SPACE_SIZE[1] - 1

# A lapát kezdeti sebessége
rect_change_x = 0
rect_change_y = 0

rect_size_x = 5
rect_size_to_sides_x = rect_size_x // 2
rect_size_y = 1

# A labda kezdeti helyzete
ball_x = SPACE_SIZE[0] // 2
ball_y = 1

# A labda sebessége
ball_change_x = 1
ball_change_y = 1
ball_size_to_sides = 1

state_to_id = {}

num_states = SPACE_SIZE[0] *SPACE_SIZE[1]* SPACE_SIZE[0]*SPACE_SIZE[1]*2*2

# képernyő méret
screen = 0

# Agent
agent = None

def drawrect(screen,x,y):
    pygame.draw.rect(screen,RED,[(x-rect_size_to_sides_x)* ZOOM_SIZE,y * ZOOM_SIZE, ZOOM_SIZE * rect_change_x, ZOOM_SIZE])

def encode_state(ball_x,ball_y,rect_x,rect_y,ball_change_x,ball_change_y):
    """Kódolja az adott állapotot"""
    return(ball_x,ball_y,rect_x,rect_y,ball_change_x,ball_change_y)

def reset():
    """visszaállítja a globális változókat"""
    global ball_change_x
    global ball_change_x
    global ball_size_to_sides
    global ball_x
    global ball_y
    global rect_x
    global rect_y
    global rect_change_x
    global rect_change_y

    # Labda mozgásának visszaállítása
    ball_change_x = 1
    ball_change_y = 1
    ball_size_to_sides = 1

    # labda helyzete
    ball_x = SPACE_SIZE[0] // 2
    ball_y = 1

    #lapát kezdő koo
    rect_x = SPACE_SIZE[0] // 2
    rect_y = SPACE_SIZE[1] - 1

    # lapát kezdő sebessége
    rect_change_x = 0
    rect_change_y = 0

def init_pong():
    """Játék inicializálása"""
    global screen
    global clock

    pygame.init()

    # A kijelző ablak inicializálása
    size = (SPACE_SIZE[0] * ZOOM_SIZE, SPACE_SIZE[1]*ZOOM_SIZE)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("pong")

    clock = pygame.time.Clock()

    print("Pong init")

## 12. órán eddig kellett másoljuk
# -----------------------------------------------------------
## 13. óra