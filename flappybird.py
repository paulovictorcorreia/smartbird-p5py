from p5 import *
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, "./" )

import numpy as np

from lib.neuralnetwork import NeuralNetwork
from models.Bird import Bird
from models.Pipe import Pipe



bird = None
pipes = []
gamestate = True
count = 0

def setup():
    size(400, 600)
    startGame()
    pipes.append(Pipe())

def draw():
    background(118,88,152)
    global bird, pipes, gamestate, count
    for i in range(len(pipes)-1, -1, -1):
        pipes[i].show()
        pipes[i].update()
        if pipes[i].hits(bird):
            gamestate = False
            for i in range(len(pipes)):
                pipes[i].stopAnimation()

        if pipes[i].offscreen():
            pipes.pop(i)
            bird.scoreAgain()
    #Condition to stop game if player dies
    #Used when there is no generic algorithm running
    if frame_count % 45 == 0 and gamestate:
        pipes.append(Pipe())
    bird.update(gamestate)
    bird.show()
    bird.edges()
    if bird.scored(pipes) and gamestate:
        count += 1
        print(bird.score)
    
    fill(255)
    text(f"Score: {count}", (30, 30))


def key_pressed():
    global bird, gamestate
    if (key == ' '):
        bird.up()

def mouse_pressed():
    global gamestate, pipes, bird
    if gamestate == False:
        gamestate = True
        pipes = []
        bird = None
        startGame()

def startGame():
    global bird, count
    bird = Bird()
    count = 0

if __name__ == '__main__':
    run(frame_rate=60)

