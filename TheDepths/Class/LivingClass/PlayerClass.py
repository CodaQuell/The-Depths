#imports 3rd party lib
import random
#imports living thing class
from Class.LivingClass.LivingThingClass import LivingThing
from Class.NonLivingClass.PotionClass import Potion
from Dictionaries.PotionDictionary import potion_inv, health_potion, strength_potion, invisibility_potion

#player class, name, age, and others
class Player(LivingThing):
    def __init__(self,name):
        self.name = name
        self.health = 10
        self.status = 0
        #status:
        #0 = normal
        #1 = confonted
        self.player_damage = random.randint(1,2)
        self.heal_mod = 0
        self.heal_difc_mod = 0
        self.hurt_difc_mod = 0
        self.heal_mod = 0
        self.hurt_mod = 0
        self.difc = " "
        self.player_xp = 0
        self.player_xp_level = 0
        self.potion_strength = 0
        self.potion_strength_count = 0
        self.potion_invisibility_count = 0


    #help func
    def help(self,monster):
        print(">> Help <<: Brings up the action menu")
        print(">> Stats <<: brings up your stats")
        print(">> Explore <<: allows you to explore the world")
        print(">> Fight <<: Allows you to fight monsters")

    #stats func
    def stats(self,monster):
        print(f">> Name: {self.name}")
        print(f">> Health: {self.health}")

    #explore func
    def explore(self,monster):
        self.heal()
        print('Your health is now', self.health)
        #if random number between 0 - 1 is 1, fight monster
        if random.randint(0,1) == 1:
            print(monster.name, 'confronts you')
            print('What do you do')
            #sets player status to fight monster
            self.status = 1

    #fight func
    def fight(self,monster):
        #check if player can fight
        if self.status == 1:
            self.hurt(monster.monster_damage + self.hurt_difc_mod)
            monster.hurt(self.player_damage + self.hurt_mod)
            print(monster.name,'attacks you')
            if self.health <= 0:
                print('You were killed by the',monster.name)
            elif monster.health > 0:
                print('You survived the', monster.name)
                print('Your health is now', self.health)
                print('The monsters health is now', monster.health)

            else:
                print('Victory! You defeated the', monster.name)
                #if fight is won set status to 0
                self.status = 0
        else:
            print('You are safe. Not a monster in sight anywhere!')

    #kill func for testing
    def kill(self,monster):
        self.health = 0
        print(f"{self.name} commited suicide")

    def use(self, monster):
        while True:
            i = input("To see a list of potions you can use type potions. \nWhat Potions would you like to use >>  ")
            if i == "potions":
                print('')
                print(">> Potions <<")
                print(">> Health Potion: Will heal you to full health << You have " + str(potion_inv.count(health_potion)) + " Health Potions")
                print(">> Strength Potion: Give you strength << You have " + str(potion_inv.count(strength_potion)) + " Strength Potions")
                print(">> Invisibility Potion: makes you invisbale << You have " + str(potion_inv.count(invisibility_potion)) + " Invisibility Potions")
                print('')

            elif i == "health potion":
                self.health += 10
                potion_inv.remove(health_potion)
                print(f"You used a health potion, your health is now {self.health}")
                break

            elif i == "strength potion":
                t = random.randint(3,5)
                while t > 0:
                    self.hurt_mod += random.randint(5,7)
                    potion_inv.remove(strength_potion)
                    print(f"You used a strength potion, you now do 5 - 7 more damage for {t} turns. You now have {potion_inv.count(strength_potion)} strength potions left.")

            else:
                print("You don't have any Health Potions")
                print("Type exit to return to the last options")                    
                break