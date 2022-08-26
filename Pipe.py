import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position,pipeGap,scrollSpeed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/pipe.png')
        self.rect = self.image.get_rect()
        self.scrollSpeed = scrollSpeed
        #position 1 is from the top, -1 is from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipeGap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(pipeGap / 2)]

    def update(self):
        self.rect.x -= self.scrollSpeed
        if self.rect.right < 60:
            self.kill()

          