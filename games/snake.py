import pygame as pg
import random
import csv
import datetime

class Snake :

    def __init__ (self, player) :

        pg.init()
        #### Creating screen ####
        self.player = player
        self.screen_width = 1000
        self.screen_height = 1000
        assert self.screen_width % 25 == 0 and self.screen_height % 25 == 0
        self.screen = pg.display.set_mode ((self.screen_width, self.screen_height))
        pg.display.set_caption('Snake')
        self.font = pg.font.Font('freesansbold.ttf', 24)

        #### Squares ####
        self.side = 25
        self.dimensions = (self.side, self.side)

        #### Snake attributes ####
        self.color = (0, 255, 0)
        self.parts = [(self.screen_width//2, self.screen_height//2)]
        self.direction = 'left'

        #### Apple attributes ####
        self.apple_color = (255, 0, 0)
        self.apple = None
        while self.apple in self.parts or self.apple == None:
            x_possible = list(range(0, self.screen_width-self.side+1, 25))
            y_possible = list(range(0, self.screen_width - self.side + 1, 25))
            self.apple = (random.choice(x_possible), random.choice(y_possible))

        self.is_running = True
        self.speed = 100 # refresh time in ms
        self.score = 0

    def eaten (self) :
        return self.apple in self.parts

    def apply_eaten (self) :
        self.score += 1
        compare = self.parts[-1]
        if len(self.parts) == 1 :
            if self.direction == 'up' :
                self.parts.append ((compare[0], compare[1]+self.side))
            elif self.direction == 'down' :
                self.parts.append((compare[0], compare[1]-self.side))
            elif self.direction == 'left' :
                self.parts.append((compare[0]+self.side, compare[1]))
            else :
                self.parts.append((compare[0]-self.side, compare[1]))
        else :
            if self.parts[-1][0] == self.parts[-2][0] + self.side :
                self.parts.append ((self.parts[-1][0] + self.side, self.parts[-1][1]))
            elif self.parts[-1][0] == self.parts[-2][0] - self.side :
                self.parts.append ((self.parts[-1][0] - self.side, self.parts[-1][1]))
            elif self.parts[-1][1] == self.parts[-2][1] + self.side:
                self.parts.append ((self.parts[-1][0], self.parts[-1][1] + self.side))
            else :
                self.parts.append ((self.parts[-1][0], self.parts[-1][1] - self.side))
        while self.apple in self.parts :
            x_possible = list(range(0, self.screen_width - self.side + 1, 25))
            y_possible = list(range(0, self.screen_width - self.side + 1, 25))
            self.apple = (random.choice(x_possible), random.choice(y_possible))

    def move (self) :
        rest = [(x[0], x[1]) for x in self.parts[:-1]]
        if self.direction == 'up' :
            change = [(self.parts[0][0], self.parts[0][1]-self.side)]
            self.parts = change + rest
        elif self.direction == 'down' :
            change = [(self.parts[0][0], self.parts[0][1]+self.side)]
            self.parts = change + rest
        elif self.direction == 'left' :
            change = [(self.parts[0][0]-self.side, self.parts[0][1])]
            self.parts = change + rest
        else :
            change = [(self.parts[0][0]+self.side, self.parts[0][1])]
            self.parts = change + rest

    def keyboard_input (self) :
        for evt in pg.event.get() :
            if evt.type == pg.QUIT:
                self.is_running = False
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] :
            self.direction = 'up'
        elif keys[pg.K_DOWN] :
            self.direction = 'down'
        elif keys[pg.K_LEFT] :
            self.direction = 'left'
        elif keys[pg.K_RIGHT] :
            self.direction = 'right'

    def dead (self) :
        x_walls = self.parts[0][0] < 0 or self.parts[0][0] > self.screen_width - self.side
        y_walls = self.parts[0][1] < 0 or self.parts[0][1] > self.screen_height - self.side
        walls = x_walls or y_walls
        itself = list(dict.fromkeys(self.parts)) != self.parts
        return walls or itself

    def apply_dead (self) :
        if self.score > 0 :
            with open ('/home/leo/Bureau/Autres/data_sets/snake_scores.csv', 'a') as file :
                writer = csv.writer(file)
                now = datetime.datetime.now()
                writer.writerow([now.strftime('%d/%m/%y-%H:%M:%S'), self.player, self.score])
        self.__init__(self.player)

    def display (self) :
        self.screen.fill((0, 0, 0))
        pg.draw.rect(self.screen, self.apple_color, self.apple + self.dimensions)
        for i in self.parts :
            i += self.dimensions
            pg.draw.rect(self.screen, self.color, i)
        score = self.font.render(f'Score : {self.score}', True, (255, 255, 255))
        self.screen.blit(score, (10, 10))
        pg.display.update()

    def play (self) :
        self.keyboard_input()
        if self.eaten() :
            self.apply_eaten()
        if self.dead () :
            self.apply_dead()
        self.move()
        self.display ()

if __name__ == '__main__' :
    player = input ('Enter your name : ')
    player = player.replace (' ', '').replace('é', 'e').lower()
    snake = Snake (player)
    while snake.is_running :
        pg.time.delay(snake.speed)
        snake.play ()
    pg.quit()