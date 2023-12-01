#imports 3rd party lib
import random

#class living thing, base for other living items
class LivingThing():
    #inits class
    def __init__(self):
        self.name =''
        self.health = 1
    #damage func
    def hurt(self):
        self.health = self.health - random.randint(0,self.health)
    #heal func
    def heal(self):
        self.health = self.health + 1