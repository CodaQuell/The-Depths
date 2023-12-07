#imports 3rd party lib
import random
#imports living thing class
from Class.LivingClass.LivingThingClass import LivingThing
from Class.LivingClass.MonsterClass import Monster
from Class.NonLivingClass.PotionClass import Potion
from Dictionaries.PotionDictionary import Potions, health_potion, strength_potion, invisibility_potion
from Dictionaries.MonsterDictionary import Monsters

#player class, name, age, and others
class Player(LivingThing):
    def __init__(self,name):
        self.name = name
        self.health = 10
        self.full_health = 10
        self.status = 0
        #status:
        #0 = normal
        #1 = confonted
        self.player_damage = random.randint(1,2)
        self.difc = " "
        self.player_xp = 0
        self.xp_level = 0
        self.new_xp_level = 10
        self.potion_status = 0
        #potion status:
        #0 = normal
        #1 = strength
        #2 = invisable


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
        print(f">> Level: {self.xp_level}")
        print(f">> XP to next level: {self.player_xp}/{self.new_xp_level}")

    #explore func
    def explore(self,monster):
        self.heal()
        print('Your health is now', self.health)
        #if random number between 0 - 1 is 1, fight monster
        if 1 == 1:
            print(monster.name, 'confronts you')
            print('What do you do')
            #sets player status to fight monster
            self.status = 1

    #fight func
    def fight(self,monster):
        if self.status == 1:
            if self.potion_status == 2:
                monster.hurt(self.player_damage)
                print(f"You are invisible, {monster.name} cannot hurt you")
                invisibility_potion.Potionsisibility_count -= 1

                if invisibility_potion.Potionsisibility_count <= 0:
                    self.potion_status = 0
                    print("You no longer have invisibility")
            else:
                if self.potion_status == 1:
                    monster.hurt(self.player_damage)
                    monster.hurt(strength_potion.potion_strength_damage)
                    print(f"You have strength, you did extra damage to {monster.name}")
                    self.hurt(monster.monster_damage)
                    strength_potion.potion_strength_count -= 1

                    if strength_potion.potion_strength_count <= 0:
                        self.potion_status = 0
                        print("You no longer have strength")
                else:
                    monster.hurt(self.player_damage)
                    self.hurt(monster.monster_damage)

            if self.health <= 0:
                print(f"You were killed by {monster.name}")

            if monster.health > 0:
                print(f"You survived the attach from {monster.name}, you now have {self.health} health \n{monster.name} has {monster.health} health")

            else:
                print(f"You killed {monster.name}")
                self.stats = 0
                self.player_xp += monster.monster_xp
                while self.player_xp >= self.new_xp_level:
                    self.xp_level += 1
                    self.new_xp_level *= 2
                    print(f"You level up, you are now level {self.xp_level}!")
                


    #kill func for testing
    def kill(self,monster):
        self.health = 0
        print(f"{self.name} commited suicide")

    def use(self, monster):
        while True:
            i = input("To see a list of potions you can use type potions. \nWhat Potions would you like to use >>  ")
            i = i.lower()
            # checks what potion that want to use
            if i == "invisibility potion":
                # checks if the potion is in the item list
                if invisibility_potion in Potions:
                    # sets the effect status to the potion effect
                    self.potion_status = 2
                    invisibility_potion.Potionsisibility_count += random.randint(2,3)
                    print(f"You are now invisable for {invisibility_potion.Potionsisibility_count} turns")
                    # removes the potion from the players inventory
                    Potions.remove(invisibility_potion)
                    # stops the loop
                    break
                else:
                    # if you dont own an Invisibility Potions
                    print("You don't have any Invisibility Potions")
                    print("Type exit to return to the last options")
                    break
            # checks for different potion name
            elif i == "strength potion":
                if strength_potion in Potions:
                    #adds to your potions effect
                    self.potion_status = 1
                    strength_potion.potion_strength_count += random.randint(2,4)
                    print(f"You used a {i} potion, you now have strength for {strength_potion.potion_strength_count} turns")
                    #removes it from the list
                    Potions.remove(strength_potion)
                    break
                else:
                    #to chatch error if no potion in item list
                    print("You don't have any Strength Potions")
                    print("Type exit to return to the last options")
                    break
            elif i == "health potion":
                if health_potion in Potions:
                    #makes health full again
                    self.full_health += 10
                    self.health = self.full_health
                    print(f"You used a health potion, your health is now {self.health}")
                    #removes it from the list
                    Potions.remove(health_potion)
                    break
                else:
                    print("You don't have any Health Potions")
                    print("Type exit to return to the last options")                    
                    break

                
                

            else:
                print(f"You don't have any {i}s left")
                print("Type exit to return to the last options")                    
                break

