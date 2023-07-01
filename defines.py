
import time,os
from pynput import keyboard
import curses


class snake:
    def __init__(self, x=0, y=0,direction="down"):
        self.length = 1
        self.x = x
        self.y = y
        self.direction = direction
        



def currentScreen(snake,screenX,screenY,foodX,foodY):
    screen = [["-"]*screenX for _ in range(screenY)]
    screen[snake.y%screenY][snake.x%screenX] = "s"
    screen[foodY][foodX] = "o"
    return screen

def printScreen(screen):
    os.system('clear')
    print('\n'.join(' '.join(map(str, row)) for row in screen),end="\r")
   
def on_press(key):
    global mode
    if key == keyboard.Key.up:
        mode = "up"
    elif key == keyboard.Key.down:
        mode = "down"
    elif key == keyboard.Key.left:
        mode = "left"
    elif key == keyboard.Key.right:
        mode = "right"
    

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False



mode="down"
pastPos = []
snakePlayer = snake()


screen = curses.initscr()
window = curses.newwin(10,10)
window.nodelay(1)
directionDict: dict = {curses.KEY_RIGHT: "right", curses.KEY_LEFT:"left",
                        curses.KEY_UP:"up", curses.KEY_DOWN:"down"}


window.keypad(True)


while True:
    char = window.getch()
    window.clear()
    window.addch(snakePlayer.y%9, snakePlayer.x%9, "s")
    
    if char == 113: break  # q
    elif char == curses.KEY_RIGHT: snakePlayer.direction = "right"
    elif char == curses.KEY_LEFT: snakePlayer.direction = "left"
    elif char == curses.KEY_UP: snakePlayer.direction = "up"
    elif char == curses.KEY_DOWN: snakePlayer.direction = "down"

    if snakePlayer.direction == "up": snakePlayer.y -=1
    elif snakePlayer.direction == "down": snakePlayer.y +=1
    elif snakePlayer.direction == "left": snakePlayer.x -=1
    elif snakePlayer.direction == "right": snakePlayer.x +=1

    curses.napms(50)
    window.addstr(0,0,str(char))


    


#printScreen(currentScreen(snakePlayer,30,10,4,4))
#time.sleep(0.1)
