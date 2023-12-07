#imports 3rd party lib
import random
#imports living thing class
from Class.LivingClass.LivingThingClass import LivingThing

#class for all monsters
class Monster(LivingThing):
    def __init__(self,name,health,monster_damage,monster_xp):
        self.name = name
        self.health = health
        self.monster_damage = monster_damage
        self.monster_xp = monster_xp
