
import time,os
from pynput import keyboard
import curses
from random import randrange

class snake:
    def __init__(self, x=0, y=0,direction="down"):
        self.length = 1
        self.x = x
        self.y = y
        self.direction = direction
        


spawnFoodCoords = lambda xWidth, yWidth: (randrange(xWidth-1), randrange(yWidth-1))





mode="down"
pastPos = []
snakePlayer = snake()


screen = curses.initscr()
max_y,max_x = screen.getmaxyx()
window = curses.newwin(max_y,max_x)
window.nodelay(1)
directionDict: dict = {curses.KEY_RIGHT: "right", curses.KEY_LEFT:"left",
                        curses.KEY_UP:"up", curses.KEY_DOWN:"down"}


window.keypad(True)
curses.curs_set(0)


prevSquares = []
foodCoords = spawnFoodCoords(max_x,max_y)
while True:
    char = window.getch()
    window.clear()
    
    window.addch(foodCoords[1]%(max_y-1), foodCoords[0]%(max_x-1), "0")

    prevSquares.append( (snakePlayer.x,snakePlayer.y) )
    if snakePlayer.length < len(prevSquares):
        prevSquares.pop(0)

    for i in prevSquares:
        window.addch(i[1]%(max_y-1), i[0]%(max_x-1), "s")
    

    if char == 113: break  # q
    elif char == curses.KEY_RIGHT: snakePlayer.direction = "right"
    elif char == curses.KEY_LEFT: snakePlayer.direction = "left"
    elif char == curses.KEY_UP: snakePlayer.direction = "up"
    elif char == curses.KEY_DOWN: snakePlayer.direction = "down"

    if snakePlayer.direction == "up": snakePlayer.y -=1
    elif snakePlayer.direction == "down": snakePlayer.y +=1
    elif snakePlayer.direction == "left": snakePlayer.x -=1
    elif snakePlayer.direction == "right": snakePlayer.x +=1

    if (snakePlayer.x,snakePlayer.y) in prevSquares:
        curses.beep()
        break
    elif (snakePlayer.x%(max_x-1),snakePlayer.y%(max_y-1)) == foodCoords:
        snakePlayer.length +=1
        foodCoords = spawnFoodCoords(max_x,max_y)
        curses.beep()

    curses.napms(50)



    


#printScreen(currentScreen(snakePlayer,30,10,4,4))
#time.sleep(0.1)
