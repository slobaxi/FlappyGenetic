from tkinter.ttk import LabelFrame
from Game import *
import Genetic
import pygame




generation = 0
prevGeneration = None 
while True:
    prevGeneration = runGame(1,generation,prevGeneration)
    print(generation)
    generation+=1

 