import Bird
import random
import numpy 
from NeuralNetwork import NeuralNetwork 
import pygame


def pick_one(birds):
    index = 0
    r = random.random()
    while r > 0:
        if(index == len(birds)):
            index = 0
        r = r - birds.sprites()[index].fitness
        index += 1
    index -= 1
    bird = birds.sprites()[index]
    child = Bird.Bird(100, int(936 / 2),neuralNetwork = bird.neuralNetwork.copy())
    child.fitness = bird.fitness
    child.mutate()
    return child

def mutate(rate):    
    def mutatedAygemnted(val):
        if random.random() < rate:
                return val + float(numpy.random.normal(0, 0.1))
        else:
            return val           
    return mutatedAygemnted

def next_gen(birds, keep_num = 10):
    calculate_fitness(birds)
    birdsList = pygame.sprite.Group()

    for i in range (0,len(birds)):
        bird = pick_one(birds)
        birdsList.add(bird)

    return birdsList

def calculate_fitness(birds):   
    sum_v = 0
    for bird in birds:
        sum_v += bird.score

    for bird in birds:
        bird.fitness = bird.score / sum_v
        bird.score = 0        