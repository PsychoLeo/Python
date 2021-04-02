import pygame as pg
import random

pg.init()

screen_side = 800
squares = 4
speed = 125 # milliseconds
pos = [(i, j) for i in range (0,screen_side, screen_side//squares) for j in range (0,screen_side, screen_side//squares)]

assert screen_side == screen_side, 'field has to be a square'
assert not screen_side % squares and not screen_side % squares, 'squares have to be integer sized'

screen = pg.display.set_mode ((screen_side, screen_side))
pg.display.set_caption('2048')

class Field :

    def __init__ (self, screen=screen, size=4, side=screen_side) :
        self.screen = screen
        self.size = size
        self.side = side
        self.grid = []

    def move (self) :
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            for block in sorted (self.grid, key = lambda elem : elem.x, reverse=True) :
                while not (block.collide_left() or block.collide_block_left(self.grid)) :
                    block.x -= block.side
            self.grid.append (Block())
        if keys[pg.K_RIGHT] :
            for block in sorted(self.grid, key=lambda elem : elem.x) :
                while not (block.collide_right() or block.collide_block_right(self.grid)) :
                    block.x += block.side
            self.grid.append (Block())
        if keys[pg.K_UP] :
            for block in sorted(self.grid, key= lambda elem : elem.y, reverse=True) :
                while not (block.collide_up() or block.collide_block_up(self.grid)) :
                    block.y -= block.side
            self.grid.append (Block())
        if keys[pg.K_DOWN] :
            for block in sorted(self.grid, key = lambda elem : elem.y) :
                while not (block.collide_down() or block.collide_block_down(self.grid)) :
                    block.y += block.side
            self.grid.append (Block())

    def draw (self) :
        self.screen.fill ((255,255,255))
        font = pg.font.SysFont('comicsans', self.side//self.size//2)
        margin = screen_side//50
        for grid_x, grid_y in pos : # drawing grid
            pg.draw.rect (self.screen, (0,0,0), (grid_x, grid_y, self.side, self.side), margin)
        for block in self.grid : # drawing blocks
            color = (255,255,255) if block.score > 4 else (0,0,0)
            pg.draw.rect (self.screen, block.get_color(), (block.x+margin//2, block.y+margin//2, block.side-margin, block.side-margin))
            score = font.render(str(block.score), True, color)
            self.screen.blit(score, (block.x + margin, block.y + margin))

    def game_over (self) :
        if len(self.grid) >= self.size ** 2 :
            end_font = pg.font.SysFont('comicsans', screen_side//10)
            game_over_text = end_font.render ('GAME OVER!', True, (255,0,0))
            max_score = max ([block.score for block in self.grid])
            score_text = end_font.render (f'Score : {max_score}', True, (0,255,0))
            screen.fill ((0,0,0))
            screen.blit (game_over_text, (screen_side//2-game_over_text.get_width()//2, screen_side//3))
            screen.blit (score_text, (screen_side//2-score_text.get_width()//2, screen_side//2))
            pg.display.update()
            pg.time.delay (2000)
            pg.quit()

class Block :

    def __init__ (self, score=None, coords=None) :
        self.field = field
        self.side = field.side//field.size
        self.score = random.choice([2,4]) if score==None else score
        self.x, self.y = random.choice([i for i in pos if i not in [(block.x, block.y) for block in self.field.grid]])\
            if coords == None else coords

    @property
    def hitbox (self) :
        return pg.Rect (self.x, self.y, self.side, self.side)

    def get_color (self) :
        score_list = [2**i for i in range (1, 12)]
        color_list = [(232,229,216), (220,208,159), (239,147,82), (230,120,43), (241,97,73),
                      (231,63,33), (235,221,115), (241,224,91), (241,222,71), (240,217,41), (255,226,0)]
        return color_list[score_list.index(self.score)]

    def collide_left (self) :
        return self.x == 0
    def collide_right (self) :
        return self.x+self.side == self.field.side
    def collide_up (self) :
        return self.y == 0
    def collide_down (self) :
        return self.y+self.side == self.field.side

    def collide_block_left (self, grid) :
        for blockA in self.grid :
            if (blockA.x, blockA.y) in [(block.x+block.side, block.y) for block in self.grid] :
                for blockB in self.grid :
                    if (blockA.x, blockA.y) == (blockB.x-blockB.side, blockB.y) and blockA.score == blockB.score :
                        self.grid.append (Block (score=blockA.score*2, coords=(blockB.x, blockB.y)))
                        self.grid.remove (blockA)
                        self.grid.remove (blockB)
                        return True
        return False

    def collide_block_right (self, grid) :
        for blockA in self.grid:
            if (blockA.x, blockA.y) in [(block.x - block.side, block.y) for block in self.grid]:
                for blockB in self.grid:
                    if (blockA.x, blockA.y) == (blockB.x + blockB.side, blockB.y) and blockA.score == blockB.score:
                        self.grid.append(Block(score=blockA.score * 2, coords=(blockB.x, blockB.y)))
                        self.grid.remove(blockA)
                        self.grid.remove(blockB)
                        return True
        return False

    def collide_block_up (self, grid) :
        return any ([self.hitbox.colliderect(pg.Rect(block.x, block.y+1, block.side, block.side)) for block in grid\
                     if block.hitbox != self.hitbox])

    def collide_block_down (self, grid) :
        for blockA in self.grid:
            if (blockA.x, blockA.y) in [(block.x, block.y - block.side) for block in self.grid]:
                for blockB in self.grid:
                    if (blockA.x, blockA.y) == (blockB.x, blockB.y + blockB.side) and blockA.score == blockB.score:
                        self.grid.append(Block(score=blockA.score*2, coords=(blockB.x, blockB.y)))
                        self.grid.remove(blockA)
                        self.grid.remove(blockB)
                        return True
        return False


field = Field () # field instance
field.grid.append (Block()) ; field.grid.append(Block())
while True :
    screen.fill ((255,255,255))
    # quitting the game
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            pg.quit()
    # moving the blocks
    field.move()
    field.draw()
    field.game_over()
    # updating display and slowing down
    pg.display.update()
    pg.time.delay(speed)