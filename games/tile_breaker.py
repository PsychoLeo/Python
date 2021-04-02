import pygame as pg
import random
import math

### Initializing ###

pg.init()
screen_width, screen_height = 1000, 1000
screen = pg.display.set_mode((screen_width, screen_height))

### Variables ###

lives = 3
colors = {'blue':(0,0,255), 'red':(255,0,0), 'green':(0,255,0),
          'white':(255,255,255), 'black':(0,0,0)}
tile_colors = [(0,255,255), (255,0,255), (192,192,192), (128,128,128),
               (128,0,0), (128,128,0), (0,128,0), (128,0,128),(0,128,128), (0,0,128)]
num_tiles = 5

### Paddle ###

class Paddle :

    def __init__ (self, screen, x, y, width, height, speed, color)  :
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.moving = 0

    def move (self) :
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT] and self.x <= screen_width - self.width :
            self.moving = 1
        if keys[pg.K_LEFT] and self.x >= 0 :
            self.moving = -1
        if self.x < 0 :
            self.x = 0
            self.moving = 0
        if self.x > screen_width - self.width :
            self.x = screen_width - self.width
            self.moving = 0
        self.x += self.speed * self.moving

    def draw (self) :
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

### Ball ###

class Ball :

    def __init__ (self, screen, x, y, radius, x_speed, y_speed, score, color) :
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.x_moving = random.choice ([-1, 1])
        self.y_moving = 1
        self.color = color
        self.score = score

    def move (self) :
        if self.x <= 0 :
            self.x_moving = 1
        elif self.x >= screen_width - self.radius:
            self.x_moving = -1
        if self.y <= 0 :
            self.y_moving = 1
        self.x += self.x_speed * self.x_moving
        self.y += self.y_speed * self.y_moving

    def hit_paddle (self, paddle) :
        ball_rect = pg.Rect (self.x, self.y, self.radius*2, self.radius*2)
        paddle_rect = pg.Rect (paddle.x, paddle.y, paddle.width, paddle.height)
        if ball_rect.colliderect (paddle_rect) :
            self.y_moving = -1

    def hit_tile (self, tile) :
        ball_rect = pg.Rect (self.x, self.y, self.radius*2, self.radius*2)
        tile_rect = pg.Rect(tile.x, tile.y, tile.width, tile.height)
        if ball_rect.colliderect(tile_rect) :
            self.y_moving *= -1
            tile.dead = True
            self.score += 1
            self.x_speed += 1
            self.y_speed += 1

    def draw (self) :
        pg.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

### Tile ###

class Tile :

    def __init__ (self, screen, width, height, max_y, color) :
        self.screen = screen
        self.width = width
        self.height = height
        self.end_x = screen_width - self.width
        self.end_y = max_y
        self.x = random.randint(0, self.end_x)
        self.y = random.randint(0, self.end_y)
        self.color = color
        self.dead = False

    def draw (self) :
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

### Creating class instances ###

paddle = Paddle (screen=screen, x=screen_width//2, y=screen_height-50,
                 width=120, height=20, speed=15, color=colors['white'])
ball = Ball (screen=screen, x=screen_width//2+paddle.width//2,y=screen_height//2,
             radius=10, x_speed=12, y_speed=8, score=0, color=colors['white'])
tiles = [Tile(screen=screen, width=80, height=15, max_y=screen_height // 3,
                      color=random.choice(tile_colors)) for i in range(num_tiles)]

font = pg.font.SysFont('comicsans', 30)

### Main loop ###

while lives > 0 :
    screen.fill ((0,0,0))
    # Quitting game
    for event in pg.event.get () :
        if event.type == pg.QUIT :
            pg.quit ()
    # Moving everything
    if tiles == [] :
        num_tiles += 1
        tiles = [Tile(screen=screen, width=80, height=15, max_y=screen_height // 3,
                      color=random.choice(tile_colors)) for i in range(num_tiles)]
    paddle.move()
    ball.move()
    for tile in tiles :
        ball.hit_tile(tile)
        if tile.dead :
            tiles.remove (tile)
    ball.hit_paddle(paddle)
    if ball.y > screen_height :
        lives -= 1
        score = ball.score
        paddle = Paddle(screen=screen, x=screen_width // 2, y=screen_height - 50,
                        width=120, height=20, speed=15, color=colors['white'])
        ball = Ball(screen=screen, x=screen_width // 2 + paddle.width // 2,
                    y=screen_height // 2, radius=10, x_speed=12, y_speed=8, score=score, color=colors['white'])
        tiles = [Tile(screen=screen, width=80, height=15, max_y=screen_height // 3,
                      color=random.choice(tile_colors)) for i in range (num_tiles)]
    # Displaying everything
    paddle.draw()
    ball.draw()
    for tile in tiles :
        tile.draw()
    text_score = font.render(f'Score : {ball.score}', True, colors['white'])
    screen.blit (text_score, (10, 10))
    text_lives = font.render (f'Lives : {lives}', True, colors['white'])
    screen.blit (text_lives, (10, 10+text_score.get_height()))
    pg.display.update()
    pg.time.delay(50)

### Game over handling ###

font = pg.font.SysFont('comicsans', 70)
text_game_over = font.render ('GAME OVER!', True, colors['red'])
screen.fill ((0,0,0))
screen.blit (text_game_over, (screen_width//2-text_game_over.get_width()//2, screen_height//3))
pg.display.update()
pg.time.delay(2000)