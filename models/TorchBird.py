import numpy as np 
from p5 import *
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, "../" )
from lib.nntorch import *

class TorchBird:
    def __init__(self, brain=None):
        self.y = height/2
        self.x = 25
        self.radius = 40
        self.gravity = 1
        self.velocity = 0
        self.lift = -10



        # self.asset_up = load_image("assets/frame-2.png")
        # self.asset_down = load_image("assets/frame-3.png")
        self.color = 255, 75


        self.scoreFlag = False
        self.scorePoints = 1
        self.score = 0
        self.fitness = 0
        if brain == None:
            self.brain = NeuralNetworkTorch(4,np.random.randint(5, 20),2)
        else:
            self.brain = brain.copy()

    def setColor(self, color):
        self.color = color

    def mutate(self, mutationRate):
        self.brain.mutate(mutationRate)

    def show(self):
        # image_mode(CENTER)
        
        # image(self.asset_up, (self.x, self.y), size=(self.radius, self.radius))
        # image_mode(CENTER)
        no_stroke()
        fill(*self.color)
        circle((self.x, self.y), self.radius)

    def think(self, pipes):

        # Find closest pipe
        closest = None
        record = np.inf
        for i in range(len(pipes)):
            d = (pipes[i].x + pipes[i].w)  - self.x
            if d > 0 and d < record:
                record = d
                closest = pipes[i]
        if closest != None:
            inputs = []

            inputs.append(self.y)
            # inputs.append(self.velocity / 20)
            inputs.append(closest.top - self.y)
            inputs.append(closest.bottom - self.y)
            inputs.append(closest.x)

            output = self.brain.forward(inputs)
            # print(output[0])

            if output[0] > output[1]:
                self.up()

    
    def update(self, gamestate):
        self.scorePoints += 1
        self.score = (self.scorePoints)

        self.velocity += self.gravity
        self.velocity *= 0.9
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

    
    
