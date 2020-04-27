import numpy as np 
from p5 import *
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, "../" )
from lib.neuralnetwork import *

class Bird:
    def __init__(self, brain=None):
        self.y = height/2
        self.x = 25
        self.radius = 40
        self.gravity = 0.8
        self.velocity = 0
        self.lift = -10
        # self.asset_up = load_image("assets/frame-2.png")
        # self.asset_down = load_image("assets/frame-3.png")
        self.scoreFlag = False
        self.scorePoints = 0

        self.score = 0
        self.fitness = 0
        if brain == None:
            self.brain = NeuralNetwork(5,8,2)
        else:
            self.brain = brain

    def mutate(self, mutationRate):
        self.brain.mutate(mutationRate)

    def show(self):
        # image_mode(CENTER)
        
        # image(self.asset_up, (self.x, self.y), size=(self.radius, self.radius))
        # image_mode(CENTER)
        no_stroke()
        fill(255, 75)
        circle((self.x, self.y), self.radius)

    def think(self, pipes):

        # Find closest pipe
        closest = pipes[0]
        closestD = np.inf
        for i in range(len(pipes)):
            d = (pipes[i].x + pipes[i].w) - self.x
            if d < closestD and d > 0:
                closestD = pipes[i]
                closestD = d
        
        inputs = []

        inputs.append(self.y)
        inputs.append(self.velocity)
        inputs.append(closest.top)
        inputs.append(closest.bottom)
        inputs.append(closest.x)

        output = self.brain.feedforward(inputs)
        # print(output[0])

        if output[0] > 0.5 and self.velocity >= 0:
            self.up()

    
    def update(self, gamestate):
        self.score += 1

        self.velocity += self.gravity
        # self.velocity *= 0.9
        self.y += self.velocity
        

    def edges(self):
        if self.y > height:
            self.y = height
            self.velocity = 0        
        if self.y < 0:
            self.velocity = 0
            self.y = 0
    
    def up(self):
        self.velocity += self.lift

    
    def deathAnimation(self):
        self.velocity += self.gravity
        self.velocity *= 0.9
        self.y += self.velocity

    def scored(self, pipes):
        if len(pipes) == 0:
            self.scoreFlag = False
            return False
        elif (self.x > pipes[0].x + pipes[0].w) and (self.scoreFlag == False):
            self.scoreFlag = True
            self.scorePoints += 1
            return True
        else:
            return False
    
    def scoreAgain(self):
        self.scoreFlag = False

    def increaseScoreGA(self):
        # self.score += 256*self.scorePoints
        pass
    
    def offScreen(self):
        return (self.y >= height)

    
    
