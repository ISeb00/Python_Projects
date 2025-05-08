##RENAME: YourLastName_wizard_class_HW.py
##Part of Python Project: 5 points
import random
## Part 1: Character class
##  Modify Attack so that it generates a random integer from 1 to self.attack
##  and subtracts that from other.hp

## Part 2: Wizard class
## Create a derived class, Wizard that inherits the base class Character
## Use super() to bring in all the data/methods from Character
## (1) Add a parameter magic to the constructor
## (2) Add a max_hp value in the constructor that is set to the original value
##     of the wizard hp
## Add 2 methods to wizard
## (1) heal - that makes hp = max_hp
## (2) fireball - It is like the Attack method, but subtracts a random
##     integer between 1 and self.magic to other.


class Character:
    def __init__(self, name='', hp=0, attack=0):
        self.name = name
        self.hp = hp
        self.attack = attack

    #Change operator overloader to print the attack value.    
    def __str__(self):
        return "Name: " + self.name + "\nHP: " + str(self.hp) + "\nAttack: " + str(self.attack)

    def Attack(self, other):
        damage=random.randint(1,self.attack)
        other.hp-=damage
        print(self.name+' dealt '+str(damage)+' damage!')

class Wizard(Character):
    def __init__(self, name='', hp=0, attack=0, magic=0):
        super().__init__(name, hp, attack)
        self.magic = magic
        self.max_hp = hp

    def __str__(self):
        return super().__str__()+'\nMagic Attack: '+str(self.magic)

    def heal(self):
        self.hp = self.max_hp
        print(self.name+' healed to '+str(self.hp)+' HP!')

    def fireball(self, other):
        damage=random.randint(1,self.magic)
        other.hp-=damage
        print(self.name+' dealt '+str(damage)+' damage!')

##TEST with the following code###
        
"""
if __name__=="__main__":
    print("Ready...Set...Fight!")
    
    weezle=Wizard('Weezle',200,5,500)
    grognak=Character('Grognak',250,300)
    print(weezle)
    print(grognak)
    grognak.Attack(weezle)
    print(weezle)
    weezle.fireball(grognak)
    print(grognak)
    weezle.heal()
    weezle.fireball(grognak)
    print(weezle)
    print(grognak)
"""    
    
## OPTIONAL: For fun only - add a while loop to main that has them fight      
##           each other until one of their hp is less than 0.
##           It then declares the other the winner.
## print("Grognak crushes Weezle!") or print("Weezle vaporizes Grognak!")

    ##Set it so that it is a more equal fight
    #weezle=Wizard('Weezle',2000,5,500)
    #grognak=Character('Grognak',2500,450)
"""
weezle=Wizard('Weezle',2000,5,500)
grognak=Character('Grognak',2500,450)

if __name__=="__main__":
    print("Ready...Set...Fight!")
    while grognak.hp > 0 and weezle.hp > 0:        
        print(weezle)
        print(grognak)
        grognak.Attack(weezle)
        print(weezle)
        weezle.fireball(grognak)
        print(grognak)
        weezle.heal()
        weezle.fireball(grognak)
        print(weezle)
        print(grognak)
    else:
        if grognak.hp <= 0:
            print("Weezle vaporizes Grognak!")
        else:
            print("Grognak crushes Weezle!")
"""
