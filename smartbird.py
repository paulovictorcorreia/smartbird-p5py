from p5 import *
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, "./" )

import numpy as np

from lib.neuralnetwork import NeuralNetwork
from models.Pipe import *
from models.SmartBird import *
import pickle

# loads file with best overall scoring bird from all trainings
try:
    bestBirdFile = open("bestBird.pkl", "rb")
    bestBird = pickle.load(bestBirdFile)
    bestBirdScore = bestBird.score
    bestBird.setColor((255, 56, 255))
    bestBirdFile.close()

    print("Success in importing best model!")
except:
    bestBird = None
    bestBirdScore = -1


birds = []
savedBirds = []
pipes = []
gamestate = True
number_birds = 100
count = 0
generations = 1

def setup():
    size(400, 600)
    global birds, pipes, number_birds, generations, bestBirdScore
    global bestBird
    # 
    for i in range(number_birds):
        birds.append(Bird())
    print(generations)
    print(bestBirdScore)
    # pixels = load_pixels()
    # print(pixels.values)
    




def draw():
    # no_loop()
    background(118,88,152)
    global birds, pipes, count, number_birds, savedBirds
    global generations, bestBird, bestBirdScore
    if count % 60 == 0:
        pipes.append(Pipe())
    if len(birds) == 0:
        count = 0
        generations += 1
        print(generations)
        # file = open("bestBird.pkl","wb")
        # if savedBirds[0].score > bestBirdScore and bestBird != None:
        #     bestBird = Bird(savedBirds[0].brain)
        #     bestBirdScore = savedBirds[0].score
        #     print(savedBirds[0].score)
        #     bestBird.setColor((255, 56, 255))
        #     pickle.dump(bestBird, file)
        # file.close()
        nextGeneration()
        pipes = []
        pipes.append(Pipe())
        
    count += 1    
    for i in range(len(pipes)-1, -1, -1):
        pipes[i].show()
        pipes[i].update()
        for j in range(len(birds)-1, -1, -1):
            if pipes[i].hits(birds[j]):
                # birds[j].fitness -= 15
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
        # if birds[i].scored(pipes): 
        #     birds[i].increaseScoreGA()
        if birds[i].offScreen():
            savedBirds.append(birds.pop(i))
    
    # shows best bird ever trained
    # displayBestBird()
        

def displayBestBird():
    global bestBird
    try:
        bestBird.think(pipes)
        bestBird.update(gamestate)
        bestBird.show()
    except:
        pass


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
    new_bird.mutate(0.01)
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

