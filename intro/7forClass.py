import random

class Character:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hitpoints = constitution * 30 + 50
        
    def printStats(self):
        print("strength: ", self.strength)
        print("dexterity: ", self.dexterity)
        print("constitution: ", self.constitution)
        print("intelligence", self.intelligence)
        print("wisdom: ", self.wisdom)
        print("charisma: ", self.charisma)

    def printHitpoints(self):
        print("hitpoints: ", self.hitpoints)

    def attack(self):
        return random.randrange(1, self.strength + 1)

    '''
    defense: take a value as an argument. Get a random number from 1-20 and 
    if it is less than dexterity, nothing happens. Otherwise, subtract the attack value
    It is confusing that what variable subtract the attack value
    '''
    def defense(self, val):
        t = random.randrange(1, 21)
        if t >= self.dexterity:
            val - self.attack()
    
    def heal(self, val):
        self.hitpoints += val

if __name__ == "__main__":
    c1 = Character(12,13,9,10,7,10)
    c1.printHitpoints()
    c1.printStats()
    c1.attack()
    c1.defense(10)
    c1.heal(3)
    print("___________________")
    c1.printHitpoints()
    c1.printStats()
