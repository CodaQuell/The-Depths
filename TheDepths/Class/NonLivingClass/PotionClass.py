from Class.NonLivingClass.ItemClass import Item

class Potion(Item):
    def __init__(self, name, flavour, potion_strength, potion_strength_count, potion_invisibility_count):
        self.name = ''
        self.flavour = ''
        self.potion_strength = 0
        self.potion_strength_count = 0
        self.potion_invisibility_count = 0
