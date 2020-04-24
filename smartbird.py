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
number_birds = 125
count = 0
generations = 1

def setup():
    size(400, 600)
    global birds, pipes, number_birds, generations
    for i in range(number_birds):
        birds.append(Bird())
    print(generations)



def draw():
    background(118,88,152)
    global birds, pipes, count, number_birds, savedBirds, generations

    if count % 75 == 0:
        pipes.append(Pipe())

    if len(birds) == 0:
        count = 0
        generations += 1
        print(generations)
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
                savedBirds.append(birds.pop(j))
            if pipes[i].offscreen():
                pipes.pop(i)
                birds[j].scoreAgain()
    
    for i in range(len(birds)):
        birds[i].think(pipes)
        birds[i].update(gamestate)
        birds[i].show()
        birds[i].edges()
    # print(len(birds))


def nextGeneration():
    global birds, number_birds, savedBirds
    birds = []
    calculateFitness()
    for i in range(number_birds):
        birds.append(pickOne())
    savedBirds = []

def pickOne():
    global savedBirds, birds
    probability = []
    for i in range(len(savedBirds)):
        prob = savedBirds[i].fitness
        probability.append(prob)
    child = np.random.choice(savedBirds, p=probability)
    brain = child.brain
    new_bird = Bird(brain)
    new_bird.mutate(0.01)
    return new_bird

def calculateFitness():
    global savedBirds
    sum_score = 0
    for bird in savedBirds:
        sum_score += bird.score 
    for bird in savedBirds:
        bird.fitness = bird.score / sum_score


def startGame():
    global birds, gamestate, numberBirds, savedBirds
    # print("oiiiiiii?")
    pipes = []
    bird = savedBirds
    savedBirds = []
    pipes.append(Pipe())

if __name__ == '__main__':
    run(frame_rate=60)

