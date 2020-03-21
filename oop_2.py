import random

class Soldier:
    name = ''
    health = 100

    def __init__(self, name):
        self.name = name

    def attack(self, victim):
        victim.health -= 20
        print('Воин ', self.name, ' атаковал ', victim.name, ' у жертвы ', victim.health, ' здоровья')


s1 = Soldier('Артурчик')
s2 = Soldier('Коловрат')


while(s1.health > 0 or s2.health > 0):
    r = random.randint(0, 1)
    if(r == 0):
        if(s1.health != 0):
            s1.attack(s2)
    else:
        if(s2.health != 0):
            s2.attack(s1)
