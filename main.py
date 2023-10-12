# Making objects interact with each other without worry about scope 
class Monster:
    def __init__ (self,health,energy, **kwargs):
        # health = 50
        # energy = 100
        print(kwargs)
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)

    def attack(self,amount):
        print('Monster has attacked')
        print(f'{amount}% damage was dealt')
        self.energy -= 20

    def move(self,speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

class Fish():
    def __init__(self, speed, has_scales):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__()

    def swim(self):
        print(f'The fish is swimming at speed of {self.speed}')

class Shark(Monster,Fish):
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        self.bite_strength= bite_strength
        super().__init__(health=health, energy=energy, speed=speed, has_scales=has_scales)


shark = Shark(50, 200, 55, 120, False)
print(shark.speed)