#version 1.0

#import 3rd party libs
import random

#import class, dictionary and function files into main
from Class.LivingThingClass import LivingThing
from Class.PlayerClass import Player
from Class.MonsterClass import Monster
from Dictionaries.CommandDictionary import Commands
from Dictionaries.MonsterDictionary import monsters
from Function.WelcomeFunc import welcome
from Function.CreditsFunc import final_credits

welcome()
#gets players name
name = input('What is your name? ')
hero = Player(name)

#gets monster to fight
monster = random.choice(monsters)

print(' (type help to get a list of actions) ')
print(hero.name,'enters a dark cave, searching for adventure. you will soon face the', monster.name)

#game loop where commands are executed
while hero.health > 0 and monster.health > 0:
    line = input('What do you want to do? >>')
    if line in Commands.keys():
        Commands[line](hero,monster)
    else:
        print(hero.name,'does not understand this suggestion.')

#runs credits
final_credits()