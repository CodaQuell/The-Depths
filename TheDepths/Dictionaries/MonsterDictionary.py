#import 3rd party lib
import random
#imports monster class
from Class.LivingClass.MonsterClass import Monster

#defines monster name and health
NewBaseMonster = Monster(
    'New Base Monster',
    10,
    1,
    0
)

#creats and adds monster to empty array
monsters = []
monsters.append(NewBaseMonster)
