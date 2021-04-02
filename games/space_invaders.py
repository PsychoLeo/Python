import pygame as pg
import random

class SpaceInvaders :

    def __init__ (self) :

        #### Screen informations ####
        self.width = 800
        self.height = 600

        #### Initializing pygame & screen ####
        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height)) # creating screen object

        #### Game images / fonts ####
        self.background = pg.image.load ('/home/leo/Images/autres/space_background.jpg')
        self.explosion = pg.image.load ('/home/leo/Images/autres/explosion.png')
        self.font = pg.font.Font ('freesansbold.ttf', 24)
        # self.game_over_music = mixer.Sound('/home/leo/Bureau/Autres/sound_sets/default_dance.wav')

        #### Player informations ####
        self.playerIm = pg.image.load ('/home/leo/Images/autres/true_beanos.ico') # getting spaceship image
        self.x = 370 # spaceship x coordinate
        self.y = 520 # spaceship y coordinate
        self.dx = 0 # x-variation
        self.speed = 0.5 # spaceship moving speed

        #### Enemy informations ####
        self.enemyIm = pg.image.load ('/home/leo/Images/autres/windows_icon.png') # getting enemy image
        self.xE = random.randint (0, self.width - 64)
        self.yE = random.randint(20, 80) # initializing y coordinate at the top of the screen
        self.yspeedE = 0.2 # enemy y-axis moving speed
        self.xspeedE = random.choice ([0.4, -0.4]) # enemy x-axis moving speed

        #### Bullet information ####
        self.bulletIm = pg.image.load ('/home/leo/Images/autres/mini_beanos.ico') # getting bullet image
        self.xB = 0
        self.yB = 0
        self.yspeedB = 1.4 # bullet speed
        self.Bstate = False # bullet is ready to be fired (True) / is fired (True)

        #### Game variables ####
        self.is_running = True # if program is running
        self.game_over = False # if enemy came down
        self.score = 0 # score variable


    def keyboard_input (self) :
        for event in pg.event.get(): # get all keys pressed
            if event.type == pg.QUIT: # quit button is pressed
                self.is_running = False
            if event.type == pg.KEYDOWN : # any key is pressed
                if event.key == pg.K_LEFT :
                    self.dx = -self.speed # left arrow key >> go left
                if event.key == pg.K_RIGHT :
                    self.dx = self.speed # right arrow key >> go right
                if event.key == pg.K_SPACE and self.Bstate == False :
                    self.xB = self.x + 16
                    self.yB = self.y + 10
                    self.Bstate = True # bullet should fire


    def handle_player_position (self) :
        if self.x >= 0 and self.x <= self.width - 64 : # between 2 sides
            self.x += self.dx # moving side indicated by keyboard input
        elif self.x < 0 :
            self.dx = 0
            self.x = 0 # avoid ship escaping left side
        else :
            self.dx = 0
            self.x = self.width - 64 # avoid ship escaping right side

    def handle_enemy_position (self) :
        if self.xE >= 0 and self.xE <= self.width - 64 : # between 2 sides
            self.xE += self.xspeedE # moving side indicated by keyboard input
        elif self.xE < 0 :
            self.xspeedE = -self.xspeedE
            self.xE = 0 # avoid ship escaping left side
        else :
            self.xspeedE = -self.xspeedE
            self.xE = self.width - 64 # avoid ship escaping right side
        if self.yE > self.y - 64 : # enemy passed through ship
            self.game_over = True
        else :
            self.yE += self.yspeedE

    def fire_bullet (self) :
        if self.yB >= 0 : # if bullet has been fired
            self.yB -= self.yspeedB # go upwards
        else : # clear bullet
            self.xB = 0
            self.yB = 0
            self.Bstate = False

    def show_score (self) :
        score = self.font.render (f'Score : {self.score}', True, (255, 255, 255)) # prints out the score
        self.screen.blit (score, (10, 10)) # score displaying in the upper left corner

    def update_screen (self):
        #### Drawing enemy and player spaceship ####
        self.screen.fill((0, 0, 0)) # fills screen with black
        self.screen.blit (self.background, (0, 0))
        if self.hit () :
            self.screen.blit (self.explosion, (self.xE, self.yE)) # explosion animation
            self.account_hit() # taking hit into account
        self.screen.blit (self.enemyIm, (self.xE, self.yE)) # displaying enemy
        self.screen.blit (self.playerIm, (self.x, self.y)) # displaying player ship
        if self.Bstate :
            self.fire_bullet() # refreshes the bullet's position
            self.screen.blit(self.bulletIm, (self.xB, self.yB)) # showing bullet travel
        self.show_score() # displaying score
        if self.game_over :
            game_over_font = pg.font.Font ('freesansbold.ttf', 40)
            game_over = game_over_font.render ('GAME OVER !', True, (255, 255, 255))
            self.screen.blit (game_over, (200, 250))
            self.__init__ () # restart game
        pg.display.update() # updates screen

    def hit (self) :
        return int(self.xB + 16) in range(int(self.xE), int(self.xE + 64)) and \
                int(self.yB - 32) in range(int(self.yE), int(self.yE + 64))  # bullet hits enemy

    def account_hit (self) :
        self.score += 1 # increase score by 1
        #### Resetting enemy and accelerating ####
        self.xE = random.randint(0, self.width - 64)
        self.yE = random.randint(20, 80)
        self.xspeedE = random.choice ([1.025, -1.025]) * self.xspeedE
        self.yspeedE *= 1.025
        self.speed *= 1.025
        self.yspeedB *= 1.025

    def play (self) :
        #### Running all functions ####
        self.keyboard_input()
        self.handle_player_position()
        self.handle_enemy_position()
        self.update_screen()


if __name__ == '__main__' :
    game = SpaceInvaders () # creating class instance
    while game.is_running : # while quit button is not pressed
        game.play () # run main function