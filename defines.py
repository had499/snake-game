
import time,os
from pynput import keyboard
import curses
from random import randrange

class snake:
    def __init__(self, x=0, y=0,direction="down"):
        self.length = 10
        self.x = x
        self.y = y
        self.direction = direction
        self.prevSquares = []
        


spawnFoodCoords = lambda xWidth, yWidth: (randrange(xWidth-1), randrange(yWidth-1))


snakePlayer = snake()


screen = curses.initscr()
max_y,max_x = screen.getmaxyx()
window = curses.newwin(max_y,max_x)
window.nodelay(1)
directionDict: dict = {curses.KEY_RIGHT: "right", curses.KEY_LEFT:"left",
                        curses.KEY_UP:"up", curses.KEY_DOWN:"down"}


window.keypad(True)
curses.curs_set(0)
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

foodCoords = spawnFoodCoords(max_x,max_y)
while True:
    char = window.getch()
    window.clear()
    
    window.addch(foodCoords[1]%(max_y-1), foodCoords[0]%(max_x-1), "0")
    snakePlayer.prevSquares.append( (snakePlayer.x,snakePlayer.y) )
    if snakePlayer.length < len(snakePlayer.prevSquares):
        snakePlayer.prevSquares.pop(0)

    j=0
    for i in snakePlayer.prevSquares:
        if j==len(snakePlayer.prevSquares)-1: window.addch(i[1]%(max_y-1), i[0]%(max_x-1), "s",curses.color_pair(1))
        else: window.addch(i[1]%(max_y-1), i[0]%(max_x-1), "s")
        j+=1

    if char == 113: break  # q
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

    if (snakePlayer.x%(max_x-1),snakePlayer.y%(max_y-1)) in snakePlayer.prevSquares:
        curses.beep()
        curses.napms(1000)
        break
    elif (snakePlayer.x%(max_x-1),snakePlayer.y%(max_y-1)) == foodCoords:
        snakePlayer.length +=1
        foodCoords = spawnFoodCoords(max_x,max_y)
        curses.beep()

    curses.napms(50)

