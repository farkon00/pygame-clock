import pygame
import time
import datetime

pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont('Arial', 50)

        self.start_time = time.time()
        self.end_time = time.time() + 60
        self.time_left = 60
        
        self.tip = self.font.render("Time left", True, (0, 0, 0))
        self.tip_rect = self.tip.get_rect()

        self.time_left_text = self.font.render(str(self.time_left), True, (0, 0, 0))
        self.time_left_rect = self.time_left_text.get_rect()
        self.time_left_rect.center = self.screen.get_rect().center

        self.tip_rect.centerx = self.time_left_rect.centerx
        self.tip_rect.bottom = self.time_left_rect.top - 10

        self.screen.blit(self.time_left_text, self.time_left_rect)
        self.screen.blit(self.tip, self.tip_rect)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.time_left = self.end_time - time.time()
        if self.time_left < 0:
            self.time_left = 0
            self.running = False
        self.time_left_text = self.font.render("{:.2f}".format(self.time_left), True, (0, 0, 0))

        self.time_left_rect = self.time_left_text.get_rect()
        self.time_left_rect.center = self.screen.get_rect().center

        self.tip_rect.centerx = self.time_left_rect.centerx
        self.tip_rect.bottom = self.time_left_rect.top - 10
        

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.time_left_text, self.time_left_rect)
        self.screen.blit(self.tip, self.tip_rect)
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()