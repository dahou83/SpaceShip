import pygame
class Ship :
    '''def __init__(self , s):
        self.screen = s .screen
        self.ship = pygame.image.load('spaceship1.png')
        self.move_horiz = 305
        self.move_vert = 150'''
    def __init__(self , ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('C:\\Users\\abdoa\\projectgame\\SpaceShip\\spaceShip1.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.movingr_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update (self):
        if self.movingr_right :
            self.rect.x += 1
        if self.moving_left :
            self.rect.x -= 1
        if self.moving_up :
            self.rect.y -=1
        if self.moving_down :
            self.rect.y +=1

    def blitme(self):
        self.screen.blit(self.image , self.rect)
        #
    '''def move (self):
        self.screen.blit(self.ship,(self.move_horiz , self.move_vert))'''




