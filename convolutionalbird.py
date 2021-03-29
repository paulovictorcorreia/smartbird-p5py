# from p5 import *
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, "./" )

import numpy as np

from lib.neuralnetwork import NeuralNetwork
from models.Pipe import *
from models.ImageBird import *

birds = []
savedBirds = []
pipes = []
number_birds = 5
count = 0
generations = 1


def setup():
    size(300, 450)
    


def draw():
    background(118,88,152)
    
    # bird = ImageBird()
    # bird.show()
    with load_pixels():
        for i in ((pixels)):
            c = floor(random(255))
            pixels[i] = c

    no_loop()


if __name__ == '__main__':
    run()