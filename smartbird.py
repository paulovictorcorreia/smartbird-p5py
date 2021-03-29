from p5 import *
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, "./" )

import numpy as np

from lib.neuralnetwork import NeuralNetwork
from models.Pipe import *
from models.SmartBird import *
import pickle
from numba import njit

# loads file with best overall scoring bird from all trainings

asset_up = None
asset_down = None
birds = []
savedBirds = []
pipes = []
gamestate = True
number_birds = 20
scores = np.zeros(number_birds)
best_score = 0
count = 0
generations = 1
frame_rate = 60
mutation_rate = 0.08

def setup():
    size(400, 600)
    global birds, pipes, number_birds, generations, asset_up, asset_down
    asset_up = load_image("assets/frame-2.png")
    asset_down = load_image("assets/frame-3.png")
    for i in range(number_birds):
        birds.append(Bird())
    print(f"Generation: {generations}")

    




def draw():
    background(118,88,152)
    global birds, pipes, count, number_birds, savedBirds
    global generations, best_score
    best_score += 5
    text(f"Current Best Score is: {best_score}", (10, 50))
    if count % frame_rate == 0:
        pipes.append(Pipe())
    if len(birds) == 0:
        count = 0
        generations += 1
        print(f"Generation: {generations}")
        nextGeneration()
        pipes = []
        pipes.append(Pipe())
        
    count += 1    
    for i in range(len(pipes)-1, -1, -1):
        pipes[i].show()
        pipes[i].update()
        for j in range(len(birds)-1, -1, -1):
            if pipes[i].hits(birds[j]):
                savedBirds.append(birds.pop(j))
            if pipes[i].offscreen():
                pipes.pop(i)
                birds[j].scoreAgain()
    
    for i in range(len(birds)-1, -1, -1):
        birds[i].think(pipes,)
        birds[i].update(gamestate)
        birds[i].show(asset_up, asset_down)
        if birds[i].offScreen():
            savedBirds.append(birds.pop(i))
    
       

def nextGeneration():
    global birds, number_birds, savedBirds, best_score
    birds = []
    calculateFitness()
    for i in range(number_birds):
        birds.append(pickOne()),

    savedBirds = []
    best_score = 0



def pickOne():
    global savedBirds, mutation_rate
    index = 0
    r = np.random.random()
    # print(r)
    while r > 0:
        r = r - savedBirds[index].fitness
        index += 1
    index -= 1
    bird = savedBirds[index]
    new_bird = Bird(bird.brain)
    new_bird.mutate(mutation_rate)
    return new_bird

def calculateFitness():
    sum_score = 0
    for bird in savedBirds:
        sum_score += bird.score 
    for i in range(len(savedBirds)-1, -1, -1):
        savedBirds[i].fitness = savedBirds[i].score / sum_score


def startGame():
    global birds, gamestate, savedBirds
    pipes = []
    bird = savedBirds
    savedBirds = []
    pipes.append(Pipe())

if __name__ == '__main__':
    run(frame_rate=frame_rate)

