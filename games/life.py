import pygame as pg
from collections import Counter

pg.init()
screen_width, screen_height = 1200, 1200
screen = pg.display.set_mode((screen_width, screen_height))

cells = []
initialize = False
size = 15 # square sizes (pixels)
speed = 300 # milliseconds
pause = 0 # pause the screen

class Cell :
    global size

    def __init__ (self, cells) :
        self.size = size
        self.cells = cells
        self.dead = []
        self.born = Counter()
        self.cycles = 0

    def cycle (self) :
        self.dead, self.born = [], Counter()
        for i in self.cells :
            local = 0
            possible = [(i[0], i[1]+size), (i[0], i[1]-size), (i[0]+size, i[1]), (i[0]-size, i[1]), (i[0]-size, i[1]+size),
                        (i[0]-size, i[1]-size), (i[0]+size, i[1]+size), (i[0]+size, i[1]-size)]
            self.born.update(possible)
            for j in possible :
                if j in self.cells :
                    local += 1
            if local > 3 or local < 2 :
                self.dead.append (i)
        self.born = [i for i in self.born if self.born[i] == 3]
        self.cells = list(set(self.cells + self.born))
        for i in self.dead :
            self.cells.remove (i)


#### Always running part ####

def start () :
    font = pg.font.SysFont('comicsans', 40)
    text = font.render('Click on the cells to fill and then press enter', True, (255,255,255))
    screen.blit (text, (screen_width//2 - text.get_width()//2, screen_height//2))
    pg.display.update()
    pg.time.delay (200)
    screen.fill((0, 0, 0))

def get_init_cells (position) :
    global cells
    if find_square(position) not in cells :
        cells.append (find_square(position))
    pg.draw.rect(screen, (255, 255, 255), cells[-1]+ (size, size))
    pg.display.update()

def find_square (position) :
    position = list(position)
    while position[0] % size != 0 :
        position[0] -= 1
    while position[1] % size != 0 :
        position[1] -= 1
    return tuple(position)

def draw_grid ():
    for x in range (0, screen_width, size) :
        for y in range (0, screen_height, size) :
            rect = pg.Rect (x, y, size, size)
            pg.draw.rect (screen, (255,255,255), rect, 1)

start ()
while True :
    draw_grid()
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            pg.quit()
        if event.type == pg.MOUSEBUTTONUP :
            get_init_cells (pg.mouse.get_pos())
        if event.type == pg.KEYDOWN and event.key == pg.K_RETURN :
            initialize = True
            cell_array = Cell(cells)
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            pause += 1
    if initialize and pause % 2 == 0:
        cell_array.cycle ()
        cell_array.cycles += 1
        screen.fill ((0,0,0))
        font_cycles = pg.font.SysFont('comicsans', 30)
        text_cycles = font_cycles.render(f'Cycles : {cell_array.cycles}', True, (169,169,169))
        screen.blit (text_cycles, (5,5))
        for cell in cell_array.cells :
            pg.draw.rect(screen, (255, 255, 255), cell + (size, size))
        pg.display.update()
        pg.time.delay (speed)
    pg.time.delay(80)