import numpy as np 
from p5 import *

class Bird:
    def __init__(self):
        self.y = height/2
        self.x = 25
        self.radius = 40
        self.gravity = 0.8
        self.velocity = 0
        self.lift = -15
        self.asset_up = load_image("assets/frame-2.png")
        self.asset_down = load_image("assets/frame-3.png")
        self.scoreFlag = False


    def show(self):
        image_mode(CENTER)
        if self.velocity <= 0:
            image(self.asset_up, (self.x, self.y), size=(self.radius, self.radius))
        else:
            image(self.asset_down, (self.x, self.y), size=(self.radius, self.radius))

    def update(self, gamestate):
        if gamestate:
            self.velocity += self.gravity
            self.velocity *= 0.9
            self.y += self.velocity
        else:
            self.velocity += self.gravity * 5
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
            return True
        else:
            return False
    
    def scoreAgain(self):
        self.scoreFlag = False
    
