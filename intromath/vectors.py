# vector class and basic operations
import math as m
#import numpy as np

class vec2d:
    def __init__(self,x0,y0):
        self.x = x0
        self.y = y0

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_vec(self):
        return (self.x, self.y)

    def mag(self):
        return m.sqrt((self.x)**2 + (self.y)**2)

    def angleRad(self):
        return (m.atan(self.y/self.x))

    def angleDeg(self):
        return self.angleRad()*180/m.pi

    def __add__(self, b):
        new_x = self.x + b.x
        new_y = self.y + b.y
        return vec2d(new_x, new_y)

    def __sub__(self,b):
        new_x = self.x - b.x
        new_y = self.y - b.y
        return vec2d(new_x, new_y)

    def __rmul__(self, b):
        new_x = b*self.x
        new_y = b*self.y
        return vec2d(new_x, new_y)