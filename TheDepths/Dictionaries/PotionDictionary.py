import random

from Class.NonLivingClass.PotionClass import Potion

Potions = []

health_potion = Potion(
    "Health Potion",
    "This potion will heal you between 3 - 5 health each time you use it. Can be found from killing monsters or from chests.",
    0,
    0,
    0
)

strength_potion = Potion(
    "Strength Potion",
    "This potion will give you a damage boost for a limited number of turns, can be found from killing monsters.",
    random.randint(5,7),
    0,
    0
)

invisibility_potion = Potion(
    "Invisibilty Potion",
    "This is the rarest of the potions, can only be found in chests, grants 3-5 turns of invisibility to the use.",
    0,
    0,
    0
)

Potions.append(health_potion)
Potions.append(strength_potion)
Potions.append(invisibility_potion)