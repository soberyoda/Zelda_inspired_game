# import libraries and modules
import pygame, sys, time
from settings import *  # import everything from settings
from level import *



# main Class, basic setup

class Game:
    def __init__(self):
        # general setup

        pygame.init()  # pygame initialization
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dinosaur Adventure Game")  # window title
        self.clock = pygame.time.Clock()  # create a clock
        self.level = Level()


    def run(self):
        while True:  # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # closing pygame window
                    pygame.quit()
                    sys.exit()  # exit from python
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)  # change screen fill
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)  # control frame rate



if __name__ == "__main__":  # check if this is a main file
    game = Game()  # instance of class
    game.run()  # call method run of class Game()
