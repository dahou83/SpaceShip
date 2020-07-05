import sys
import pygame
from settings import Setting
from ShipModule import Ship

class AlienInvasion :
        '''Overall class to manage game assets and behavor'''
        def __init__(self):
            pygame.init()
            self.settings = Setting()
            self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_hight))
            pygame.display.set_caption("Alien Invision")
            icon = pygame.image.load('Png.png')
            pygame.display.set_icon(icon)
            self.screen.fill(self.settings.bg_color)
            self.ship = Ship(self)
        def run_game(self):
            while True:
                self._check_events()
                self.ship.update()
                self. _update_screen()
        def _check_events(self):
                for event in pygame.event.get():
                       if event.type ==pygame.QUIT:
                            sys.exit()
                       elif event.type == pygame.KEYDOWN :
                           if event.key == pygame.K_RIGHT :
                              self.ship.movingr_right = True
                           if event.key == pygame.K_LEFT :
                               self.ship.moving_left = True
                           if event.key == pygame.K_UP :
                               self.ship.moving_up = True
                           if event.key == pygame.K_DOWN :
                                self.ship.moving_down = True
                       elif event.type == pygame.KEYUP :
                           if event.key == pygame.K_RIGHT :
                              self.ship.movingr_right = False
                           if event.key == pygame.K_LEFT :
                               self.ship.moving_left = False
                           if event.key == pygame.K_UP :
                               self.ship.moving_up = False
                           if event.key == pygame.K_DOWN :
                                self.ship.moving_down = False
        def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
                #self.ship.move()
            pygame.display.flip()
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()



