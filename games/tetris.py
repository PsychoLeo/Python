import pygame as pg
import random
# import pprint

### Initializing ###
pg.init()

constant_delay = refresh_speed = 50 # milliseconds
refresh_change = 10 # speed decrease value each time a row is completed
fall_speed = 5 # pixels per refresh_speed
side = 40
assert side % fall_speed == 0

columns = 12
rows = 22
screen_width = columns * side # 480
screen_height = rows * side # 880
screen = pg.display.set_mode((screen_width, screen_height))

### Variables - blocks ###
blocks = ('I', 'J', 'L', 'O', 'S', 'T', 'Z')
colors = {
    'I': (0, 255, 255),
    'J': (0, 0, 255),
    'L': (255,140,0),
    'O': (255, 255, 0),
    'S': (0, 255, 0),
    'T': (128,0,128),
    'Z': (255, 0, 0)
}
forms_0 = {
    'I': [(4*side, 0), (5*side, 0), (6*side, 0), (7*side, 0)], # light blue
    'J': [(5*side, 0), (5*side, side), (6*side, side), (7*side, side)], # blue
    'L': [(7*side, 0), (5*side, side), (6*side, side), (7*side, side)], # orange
    'O': [(5*side, 0), (6*side, 0), (5*side, side), (6*side, side)], # yellow
    'S': [(6*side, 0), (7*side, 0), (5*side, side), (6*side, side)], # green
    'T': [(6*side, 0), (5*side, side), (6*side, side), (7*side, side)], # purple
    'Z': [(5*side, 0), (6*side, 0), (6*side, side), (7*side, side)] # red
}
# rotating right 90°
forms_1 = {
    'I': [(5*side, 0), (5*side, side), (5*side, 2*side), (5*side, 3*side)],
    'J': [(5*side, 0), (6*side, 0), (5*side, side), (5*side, 2*side)],
    'L': [(5*side, 0), (5*side, side), (5*side, 2*side), (6*side, 2*side)],
    'O': forms_0['O'],
    'S': [(5*side, 0), (5*side, side), (6*side, side), (6*side, 2*side)],
    'T': [(5*side, 0), (5*side, side), (6*side, side), (5*side, 2*side)],
    'Z': [(6*side, 0), (6*side, side), (5*side, side), (5*side, 2*side)]
}
forms_2 = {
    'I': forms_0['I'],
    'J': [(5*side, 0), (6*side, 0), (7*side, 0), (7*side, side)],
    'L': [(5*side, 0), (6*side, 0), (7*side, 0), (5*side, side)],
    'O': forms_0['O'],
    'S': forms_0['S'],
    'T': [(5*side, 0), (6*side, 0), (7*side, 0), (6*side, side)],
    'Z': forms_0['Z']
}
forms_3 = {
    'I': forms_1['I'],
    'J': [(6*side, 0), (6*side, side), (6*side, 2*side), (5*side, 2*side)],
    'L': [(5*side, 0), (6*side, 0), (6*side, side), (6*side, 2*side)],
    'O': forms_0['O'],
    'S': forms_1['S'],
    'T': [(6*side, 0), (6*side, side), (6*side, 2*side), (5*side, side)],
    'Z': forms_1['Z']
}

class Field :

    def __init__ (self, columns, rows) :
        self.columns = columns
        self.rows = rows
        self.grid = [[(0, None) for i in range (self.columns)] for j in range (self.rows)]
        self.score = 0

    def update (self, block) :
        global refresh_speed, refresh_change
        for x, y in zip(block.x, block.y) :
            self.grid[y//side][x//side] = (1, block.color)
        # for i in self.grid :
        #     print (i)
        for i in range (len(self.grid)) :
            if all ([self.grid[i][j][0]==1 for j in range (len(self.grid[0]))]) :
                self.score += 1
                refresh_speed -= refresh_change
                current_row = i
                for j in range (len(self.grid[0])) :
                    self.grid[i][j] = (0, None)
                while current_row > 1 :
                    for j in range (len(self.grid[0])) :
                        self.grid[current_row][j] = self.grid[current_row-1][j]
                    current_row -= 1

    def higher_blocks (self) :
        columns = [[self.grid[i][j][0] for i in range (len(self.grid))] for j in range (len(self.grid[0]))]
        res = []
        for col in range (len(columns)) :
            if 1 in columns[col] :
                res.append ((col*side, columns[col].index(1)*side)) # coords of higher blocks
        return res

    def game_over (self) :
        if 1 in [i[0] for i in self.grid[0]] :
            font = pg.font.SysFont('comicsans', 40)
            game_over_text = font.render('GAME OVER!', True, (255,0,0))
            score_text_over = font.render (f'Score : {self.score}', True, (255,255,255))
            screen.fill ((0,0,0))
            screen.blit (game_over_text, (screen_width//2 - game_over_text.get_width()//2, screen_height//2))
            screen.blit (score_text_over, (screen_width//2 - score_text_over.get_width()//2, screen_height//2+score_text_over.get_height()))
            pg.display.update()
            pg.time.delay (3000)
            pg.quit()

    def draw (self) :
        for row in range (len(self.grid)) :
            for column in range (len(self.grid[0])) :
                if self.grid[row][column][0] == 1 :
                    pg.draw.rect(screen, self.grid[row][column][1], (column*side, row*side, side, side))
                    pg.draw.rect (screen, (0,0,0), (column*side, row*side, side, side), 1)
        font = pg.font.SysFont('comicsans', 20)
        score_text = font.render (f'Score : {self.score}', True, (0,0,0))
        screen.blit (score_text, (10, 10))


class Block :

    def __init__ (self, block) :
        self.forms = (forms_0[block], forms_1[block],
                      forms_2[block], forms_3[block])
        self.color = colors[block]
        self.side = side
        self.speed = 1
        self.rotations = 0
        self.x_var, self.y_var = 0, 0
        self.fixed = False
        self.current_form = self.forms[self.rotations%4]
        self.x = [form[0] for form in self.current_form]
        self.y = [form[1] for form in self.current_form]

    def move (self) :
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and not self.collide_left():
            self.x_var -= self.side
            self.x = [x-self.side for x in self.x]
        if keys[pg.K_RIGHT] and not self.collide_right():
            self.x_var += self.side
            self.x = [x+self.side for x in self.x]
        if keys[pg.K_UP] :
            self.rotations += 1
            self.current_form = self.forms[self.rotations%4]
            self.x = [form[0]+self.x_var for form in self.current_form]
            self.y = [form[1]+self.y_var for form in self.current_form]
        if keys[pg.K_DOWN] and not (self.collide_bottom() or self.collide_blocks(field)):
            while not (self.collide_blocks(field) or self.collide_bottom()):
                self.y_var += fall_speed
                self.y = [y+fall_speed for y in self.y]

    def collide_left (self) :
        return any ([x <= 0 for x in self.x])

    def collide_right (self) :
        return any([x+self.side >= screen_width for x in self.x])

    def collide_bottom (self) :
        if any([y+self.side >= screen_height for y in self.y]) :
            self.fixed = True
            return True
        else :
            return False

    def collide_blocks (self, grid) :
        for x, y in zip(self.x, self.y) :
            block = pg.Rect (x, y, side, side+1)
            if any([block.colliderect(upper+(side, side)) for upper in grid.higher_blocks()]):
                self.fixed = True
                return True

    def draw (self) :
        surface = (self.side, self.side)
        for x, y in zip(self.x, self.y) :
            pg.draw.rect(screen, self.color, (x, y)+surface)
            pg.draw.rect (screen, (0,0,0), (x,y)+surface, 1)

font = pg.font.SysFont('comicsans', 30)

field = Field (columns, rows)
first_block = random.choice (blocks)
block = Block (first_block)
random_blocks = [first_block]

def NES_random () :
    global random_blocks, blocks
    maxi = len(blocks)
    r1, r2 = blocks.index(random_blocks[-1]), random.randint(0, maxi)
    if r1 == r2:
        r2 = random.randint (0, maxi)
    while r2 == maxi :
        r2 = random.randint(0, maxi)
    random_blocks.append (blocks[r2])
    return None

while True :
    screen.fill((255,255,255))
    field.draw()
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            pg.quit()
    if block.fixed :
        field.update (block)
        NES_random()
        block = Block (random_blocks[-1])
    else :
        if not (block.collide_bottom() or block.collide_blocks(field)) :
            block.y_var += fall_speed
            block.y = [y+fall_speed for y in block.y]
        block.move()
        block.collide_blocks(field)
        block.draw()
        field.game_over()
    pg.time.delay(constant_delay+refresh_speed)
    pg.display.update()