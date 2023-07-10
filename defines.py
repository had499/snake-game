
import curses
from random import randrange
from curses.textpad import rectangle
class snake:
    def __init__(self, x=0, y=0,direction="right"):
        self.length = 3
        self.x = x
        self.y = y
        self.direction = direction
        self.prevSquares = []
        


spawnFoodCoords = lambda xWidth, yWidth: (randrange(xWidth-1), randrange(yWidth-1))


def directionAdjust(snakePlayer, char):
    global gameOn
    if char == 113: gameOn = False  # q
    if snakePlayer.length == 1:
        match char:
            case curses.KEY_RIGHT: snakePlayer.direction = "right"
            case curses.KEY_LEFT: snakePlayer.direction = "left"
            case curses.KEY_UP: snakePlayer.direction = "up"
            case curses.KEY_DOWN: snakePlayer.direction = "down"
    else:
        if char == curses.KEY_RIGHT and not snakePlayer.direction == "left": snakePlayer.direction = "right"
        elif char == curses.KEY_LEFT and not snakePlayer.direction == "right": snakePlayer.direction = "left"
        elif char == curses.KEY_UP and not snakePlayer.direction == "down": snakePlayer.direction = "up"
        elif char == curses.KEY_DOWN and not snakePlayer.direction == "up": snakePlayer.direction = "down"

    if snakePlayer.direction == "up": snakePlayer.y -=1
    elif snakePlayer.direction == "down": snakePlayer.y +=1
    elif snakePlayer.direction == "left": snakePlayer.x -=1
    elif snakePlayer.direction == "right": snakePlayer.x +=1
    return snakePlayer


###
### Initialise player and screen
###
snakePlayer = snake()
screen = curses.initscr()
max_y,max_x = screen.getmaxyx()
window = curses.newwin(max_y,max_x)
window.nodelay(1)
window.keypad(True)
curses.curs_set(0)
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
gameOn = True




foodCoords = spawnFoodCoords(max_x,max_y)
while gameOn:
    char = window.getch()
    window.clear()
    
    window.addstr(1,1,f"score: {str(snakePlayer.length)}")

    window.addch(foodCoords[1]%(max_y-1), foodCoords[0]%(max_x-1), "0")
    snakePlayer.prevSquares.append( (snakePlayer.x%(max_x-1),snakePlayer.y%(max_y-1)) )
    if snakePlayer.length < len(snakePlayer.prevSquares):
        snakePlayer.prevSquares.pop(0)

    j=0
    for i in snakePlayer.prevSquares:
        if j==len(snakePlayer.prevSquares)-1: window.addch(i[1]%(max_y-1), i[0]%(max_x-1), "s",curses.color_pair(1))
        else: window.addch(i[1]%(max_y-1), i[0]%(max_x-1), "s")
        j+=1

    snakePlayer = directionAdjust(snakePlayer,char)

    if (snakePlayer.x%(max_x-1),snakePlayer.y%(max_y-1)) in snakePlayer.prevSquares:
        curses.beep
        curses.napms(1000)
        break
    elif (snakePlayer.x%(max_x-1),snakePlayer.y%(max_y-1)) == foodCoords:
        snakePlayer.length +=1
        foodCoords = spawnFoodCoords(max_x,max_y)
        curses.beep()

    
    curses.napms(50)

