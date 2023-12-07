#version 1.3

#import 3rd party libs
import random

#import class, dictionary and function files into main
from Class.LivingClass.LivingThingClass import LivingThing
from Class.LivingClass.PlayerClass import Player
from Class.LivingClass.MonsterClass import Monster
from Class.NonLivingClass.PotionClass import Potion
from Dictionaries.CommandDictionary import Commands
from Dictionaries.MonsterDictionary import Monsters
from Dictionaries.PotionDictionary import Potions
from Function.WelcomeFunc import WelcomeFunc
from Function.CreditsFunc import CreditsFunc
from Function.EntryFunc import EntryFunc

#gets monster to fight
monster = random.choice(Monsters)

#gets players name
print(' ')
name = input('Enter your username >>  ')
print(' ')
hero = Player(name)

while True:
    i = input("Choose a difficulty >> \n 1 >> Easy \n 2 >> Medium \n 3 >> Hard \n >>  ")
    if i == "1" or "Easy":
        print("You chose easy")
        hero.health += 20
        hero.full_health += 20
        hero.difc = "Easy"
        break
    elif i == "2" or "Medium":
        print("You chose medium")
        hero.health += 10
        hero.full_health += 10
        hero.difc = "Medium"
        break
    elif i == "3" or "Hard":
        print("You chose hard")
        hero.difc = "Hard"
        break
    else:
        print("Please choose on of the options")

print(" ")
print("Character Overview")
print(f">> Name: {hero.name}")
print(f">> Health: {hero.health}")
print(f">> Difficulty: {hero.difc}")

EntryFunc()
WelcomeFunc()

#game loop where commands are executed
while hero.health > 0:
    line = input('What do you want to do? >>  ')
    if line in Commands.keys():
        Commands[line](hero,monster)
    else:
        print(hero.name,'does not understand this suggestion.')

#runs credits
CreditsFunc()