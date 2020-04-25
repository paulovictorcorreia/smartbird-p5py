from p5 import *
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, "./" )

import numpy as np

from lib.neuralnetwork import NeuralNetwork
from models.Pipe import Pipe
from models.SmartBird import Bird



birds = []
savedBirds = []
pipes = []
gamestate = True
number_birds = 200
count = 0
generations = 1
slide = None

def setup():
    size(400, 600)
    global birds, pipes, number_birds, generations, slider
    for i in range(number_birds):
        birds.append(Bird())
    print(generations)



def draw():
    background(118,88,152)
    global birds, pipes, count, number_birds, savedBirds, generations, slider
    if count % 75 == 0:
        pipes.append(Pipe())

    if len(birds) == 0:
        count = 0
        generations += 1
        print(generations)
        # print(savedBirds[-1].score)
        nextGeneration()
        pipes = []
        pipes.append(Pipe())
    count += 1    
    for i in range(len(pipes)-1, -1, -1):
        pipes[i].show()
        pipes[i].update()
        for j in range(len(birds)-1, -1, -1):
            if pipes[i].hits(birds[j]):
                birds[j].fitness -= 15
                # print(len(birds))
                savedBirds.append(birds.pop(j))
            if pipes[i].offscreen():
                pipes.pop(i)
                birds[j].scoreAgain()
    
    for i in range(len(birds)-1, -1, -1):
        
        birds[i].think(pipes)
        birds[i].update(gamestate)
        birds[i].show()
        # birds[i].edges()
        if birds[i].scored(pipes): 
            birds[i].increaseScoreGA()
        if birds[i].offScreen():
            savedBirds.append(birds.pop(i))
        # print(len(birds))


def nextGeneration():
    global birds, number_birds, savedBirds
    birds = []
    calculateFitness()
    for i in range(number_birds):
        birds.append(pickOne()),

    savedBirds = []
    # for i in range(number_birds):
    #     print(birds[i].brain.weights_ih)
    #     print(birds[i].brain.weights_ho)
    #     print()

def pickOne():
    global savedBirds
    index = 0
    r = np.random.random()
    # print(r)
    while r > 0:
        r = r - savedBirds[index].fitness
        index += 1
    index -= 1
    bird = savedBirds[index]
    new_bird = Bird(bird.brain)
    new_bird.mutate(0.05)
    return new_bird

def calculateFitness():
    global savedBirds
    sum_score = 0
    for bird in savedBirds:
        sum_score += bird.score 
    for i in range(len(savedBirds)-1, -1, -1):
        savedBirds[i].fitness = savedBirds[i].score / sum_score


def startGame():
    global birds, gamestate, numberBirds, savedBirds
    # print("oiiiiiii?")
    pipes = []
    bird = savedBirds
    savedBirds = []
    pipes.append(Pipe())

if __name__ == '__main__':
    run(frame_rate=60)

