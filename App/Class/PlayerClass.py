#imports 3rd party lib
import random
#imports living thing class
from Class.LivingThingClass import LivingThing

#player class, name, age, and others
class Player(LivingThing):
    def __init__(self,name):
        self.name = name
        self.health = 15
        self.status = 'regular'

    #help func
    def help(self,monster):
        print(">> Help <<: Brings up the action menu")
        print(">> Stats <<: brings up your stats")
        print(">> Explore <<: allows you to explore the world")
        print(">> Fight <<: Allows you to fight monsters")

    #stats func
    def stats(self,monster):
        print('You are', self.name)
        print('With health of', self.health)
        print('Your status is', self.status)
        print(monster.name, 'health is', monster.health)

    #explore func
    def explore(self,monster):
        self.heal()
        print('Your health is now', self.health)
        #if random number between 0 - 1 is 1, fight monster
        if random.randint(0,1) == 1:
            print(monster.name, 'confronts you')
            print('What do you do')
            #sets player status to fight monster
            self.status = 'confronted'

    #fight func
    def fight(self,monster):
        #check if player can fight
        if self.status == 'confronted':
            self.hurt()
            monster.hurt()
            print(monster.name,'attacks you')
            if self.health <= 0:
                print('You were killed by the',monster.name)
            elif monster.health > 0:
                print('You survived the', monster.name)
                print('Your health is now', self.health)
                #if fight is won set status to regular
                self.status = 'regular'
            else:
                print('Victory! You defeated the', monster.name)
        else:
            print('You are safe. Not a monster in sight anywhere!')

    #kill func for testing
    def kill(self,monster):
        self.health = 0
        print(f"{self.name} commited suicide")