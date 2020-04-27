from p5 import *
import numpy as np 

class Pipe:
    def __init__(self):
        self.height = 150
        self.top = random_uniform(height/2)
        self.bottom = self.top + self.height
        self.x = width
        self.w = 75
        self.speed = 5
        
    
    def hits(self, bird):
        if (bird.y < self.top) or (bird.y > (self.top + self.height)):
            if (bird.x > self.x) and (bird.x < (self.x + self.w)):
                return True
        return False

    def show(self):
        fill(82,208,83)
        rect((self.x, 0), self.w, self.top)
        rect((self.x, self.bottom), self.w, height - self.bottom)
    
    def update(self):
        self.x -= self.speed
    
    def offscreen(self):
        if self.x < -self.w:
            return True
        else:
            return False
    
    def stopAnimation(self):
        self.speed = 0