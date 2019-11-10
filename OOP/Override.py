class Animal(object):
    def __init__(self):
        self.can_run = False
        self.can_fly = False

    def print_abilities(self):
        print(type(self).__name__ + ':')
        print('Can run:', self.can_run)
        print('Can fly: ', self.can_fly)
        print()

class Horse(Animal):
    def __int__(self):
        super().__init__()
        self.can_run = True

class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.can_fly = True

class Pegasus(Horse, Animal):
    pass

if __name__ == '__main__':
    horse = Horse()
    horse.print_abilities()

    bird = Bird()
    bird.print_abilities()

    pegasus = Pegasus()
    bird.print_abilities()