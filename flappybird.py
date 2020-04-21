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
    background(128)
    global bird, pipes, gamestate
    for i in range(len(pipes)-1, -1, -1):
        pipes[i].show()
        pipes[i].update()
        if pipes[i].hits(bird):
            gamestate = False
            for i in range(len(pipes)):
                pipes[i].stopAnimation()

        if pipes[i].offscreen():
            pipes.pop(i)
    #Condition to stop game if player dies
    #Used when there is no generic algorithm running
    if frame_count % 45 == 0 and gamestate:
        pipes.append(Pipe())
    bird.update(gamestate)
    bird.show()
    bird.edges()


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
    global bird
    bird = Bird()

if __name__ == '__main__':
    run()