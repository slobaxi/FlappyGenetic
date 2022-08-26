from os import kill
from turtle import update
import pygame
from pygame.locals import *
from Bird import Bird
from Pipe import Pipe
import random
import Genetic

     
def runGame(numberOfBirds,generation,prevGeneration = None):
    gameOver = False
    listOfDeadSprites = []
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    screenWidth = 864
    screenHeight = 936
    screen = pygame.display.set_mode((screenWidth,screenHeight))

    #load img
    background = pygame.image.load('img/bg.png')
    ground = pygame.image.load('img/ground.png')


    #    
    font = pygame.font.SysFont('Bauhaus 93', 60)
    white = (255, 255, 255)
    groundScroll = 0
    totalScore = groundScroll
    scrollSpeed = 4
    pass_pipe = False
    score = 0

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

     # create birds
    if(generation == 0):
        birdGroup = pygame.sprite.Group()
        for i in range (0,numberOfBirds):
            flappy = Bird(100, int(screenHeight / 2))
            birdGroup.add(flappy)     
    else :
        birdGroup = Genetic.next_gen(prevGeneration)   
    
    #create pipes
    pipe_gap = 150
    pipe_frequency = 1500 #milliseconds
    last_pipe = pygame.time.get_ticks() - pipe_frequency
    pipe_group = pygame.sprite.Group()


    run = True
    while run:

        clock.tick(fps)

        #draw background
        screen.blit(background,(0,0))


        #draw Birds
        birdGroup.draw(screen)
        birdGroup.update

        #draw Pipe
        pipe_group.draw(screen)

        #draw groud and move it
        screen.blit(ground,(groundScroll,768))

         #check the score
        if len(pipe_group) > 0:
            if birdGroup.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
                and birdGroup.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
                and pass_pipe == False:
                pass_pipe = True
            if pass_pipe == True:
                if birdGroup.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                    score += 1
                    pass_pipe = False

        draw_text(str(score) , font, white, int(screenWidth / 2)-50, 20)
        draw_text("Generation: " +str(generation), font, white, int(screenWidth / 2)-200, 60)

        #check if any birds colide with Pipe
        for bird in birdGroup:
            spriteGroupHelper = pygame.sprite.Group()
            spriteGroupHelper.add(bird)
            if pygame.sprite.groupcollide(spriteGroupHelper, pipe_group, False, False) or bird.rect.top < 0:
                bird.live = False

        
    

        #kill bird if it fails
        for bird in birdGroup:
            if bird.rect.bottom > 768:
                bird.live = False
                
            
        
        #draw pipes
        if gameOver == False:

            #generate new pipes
            time_now = pygame.time.get_ticks()
            if time_now - last_pipe > pipe_frequency:
                pipe_height = random.randint(-100, 100)
                btm_pipe = Pipe(screenWidth, int(screenHeight / 2) + pipe_height, -1,pipe_gap,scrollSpeed)
                top_pipe = Pipe(screenWidth, int(screenHeight / 2) + pipe_height, 1,pipe_gap,scrollSpeed)
                pipe_group.add(btm_pipe)
                pipe_group.add(top_pipe)
                last_pipe = time_now


            #draw and scroll the ground
            groundScroll = groundScroll - scrollSpeed
            totalScore = totalScore + groundScroll
            if abs(groundScroll) > 35:
                groundScroll=0

            #proslediti informije o poziciji cevi
            pipe_group.update()

        #check for game over
        gameOver = True
        for bird in birdGroup:
            if not bird.live:
                listOfDeadSprites.append(bird)
                bird.kill()         
                continue
            gameOver = False
        birdGroup.update(pipe_group.sprites()[0],pipe_group.sprites()[1])
        
        pygame.display.update()

        if(gameOver) :
            run = False
            pygame.quit()

        
    prevGeneration = birdGroup
    for bird in listOfDeadSprites:
        prevGeneration.add(bird)          
    return prevGeneration            
       
    






            