#imports 3rd party lib
import random
#imports living thing class
from Class.LivingThingClass import LivingThing

#class for all monsters
class Monster(LivingThing):
    def __init__(self,name,health):
        self.name = name
        self.health = health