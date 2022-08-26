from asyncio.windows_utils import pipe
import pygame
import NeuralNetwork
import Genetic

class Bird(pygame.sprite.Sprite):

    def __init__(self, x, y, neuralNetwork = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/bird1.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.velocity = 8
        self.score = 1
        self.fitness = 0
        self.live = True
        self.clicked = False
        self.disabled = False
        self.flap = False
        self.subtracted = False     
        if neuralNetwork == None:
            self.neuralNetwork = NeuralNetwork.NeuralNetwork(3,3,1)
        else:
            self.neuralNetwork = neuralNetwork    
        
    def mutate(self):
        self.neuralNetwork.mutate(Genetic.mutate(0.1))

    def updateHelper(self):
        self.velocity += 0.5
        if self.velocity > 8:
            self.velocity = 8
        if self.rect.bottom < 768:
            self.rect.y += int(self.velocity)
        if self.live:
            self.score = +1
            self.fitnes = +1 
            #jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.velocity = - 10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.kill()

    def update(self,pipeBtm, pipeTop):
    
        if self.rect.bottom > 768:
            self.live = False

        if self.rect.top < 0:
            self.live = False        

        #Normalize input parametars
        pipeY = (pipeTop.rect.bottomleft[1] + (pipeBtm.rect.topleft[1] - pipeTop.rect.bottomleft[1]) / 2 ) / 936
        pipeX = (pipeTop.rect.bottomleft[0]) / 864
        birdY = self.rect.bottom / 936

        if self.live and not self.clicked:    
            inputData = [birdY,pipeX,pipeY]
            #Neural networks decides wheather to jump
            if self.neuralNetwork.predict(inputData)[0][0] > 0.7:
                self.flap = True

            self.score += 1

            if not self.live:
                return

            elif self.flap == False or self.disabled:
                self.rect.y += self.velocity
            else:
                self.rect.y -= 8
        
            self.flap = False

                  


            
 

   
                                