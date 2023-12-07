#import 3rd party lib
import random
#imports monster class
from Class.LivingClass.MonsterClass import Monster

#defines monster name and health
NewBaseMonster = Monster(
    'New Base Monster',
    2,
    1,
    1
)

#creats and adds monster to empty array
Monsters = []
Monsters.append(NewBaseMonster)
