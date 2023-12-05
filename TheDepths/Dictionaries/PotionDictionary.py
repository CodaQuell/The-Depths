import random

from Class.NonLivingClass.PotionClass import Potion

potion_inv = []

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
    random.randint(5,6),
    random.randint(1,3),
    0
)

invisibility_potion = Potion(
    "Invisibilty Potion",
    "This is the rarest of the potions, can only be found in chests, grants 3-5 turns of invisibility to the use.",
    0,
    0,
    random.randint(3,5)
)

potion_inv.append(health_potion)
potion_inv.append(strength_potion)
potion_inv.append(invisibility_potion)