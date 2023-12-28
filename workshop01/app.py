class Weapon:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.level = 1

    def upgrade(self):
        self.level += 1

    def display(self):
        print(f"Weapon: {self.name}, Type: {self.type}, Level: {self.level}")

def run():
    # instances
    weapon1 = Weapon("Blade", "Melee")
    weapon2 = Weapon("Gun", "Ranged")

    # Displaying the initial state of the weapons
    weapon1.display()
    weapon2.display()

    # Upgrading one of the weapons
    weapon1.upgrade()
    weapon2.upgrade()
    print('Level Up!')
    weapon1.display()
    weapon2.display()