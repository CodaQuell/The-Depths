#version 1.1

#import 3rd party libs
import random

#import class, dictionary and function files into main
from Class.LivingClass.LivingThingClass import LivingThing
from Class.LivingClass.PlayerClass import Player
from Class.LivingClass.MonsterClass import Monster
from Class.NonLivingClass.PotionClass import Potion
from Dictionaries.CommandDictionary import Commands
from Dictionaries.MonsterDictionary import monsters
from Dictionaries.PotionDictionary import potion_inv
from Function.WelcomeFunc import welcome
from Function.CreditsFunc import final_credits

#gets monster to fight
monster = random.choice(monsters)

#while loop to get player details
while True:
    #gets players name
    print(' ')
    name = input('Enter your username >>  ')
    print(' ')
    hero = Player(name)

    while True:
        i = input("Choose a difficulty >> \n 1 >> Easy \n 2 >> Medium \n 3 >> Hard \n >>  ")
        if i == "1":
            print("You chose easy")
            hero.health += 20
            hero.heal_difc_mod += random.randint(2,4)
            hero.difc = "Easy"
            break
        elif i == "2":
            print("You chose medium")
            hero.health += 10
            hero.hurt_difc_mod += random.randint(2,3)
            hero.heal_difc_mod += 1
            hero.difc = "Medium"
            break
        elif i == "3":
            print("You chose hard")
            hero.hurt_difc_mod += random.randint(3,5)
            hero.difc = "Hard"
            break
        else:
            print("Please choose on of the options")

    print(" ")
    print("Character Overview")
    print(f">> Name: {hero.name}")
    print(f">> Health: {hero.health}")
    print(f">> Difficulty: {hero.difc}")

    print(" ")
    i = input("Type enter to start the game >>  ")
    if i == "enter":
        break
    elif i == "":
        break
    else:
        print("Please type enter to start")

welcome()

#game loop where commands are executed
while hero.health > 0 and monster.health > 0:
    line = input('What do you want to do? >>  ')
    if line in Commands.keys():
        Commands[line](hero,monster)
    else:
        print(hero.name,'does not understand this suggestion.')

#runs credits
final_credits()