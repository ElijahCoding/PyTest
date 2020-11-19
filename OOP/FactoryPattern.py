import random
from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def __init__(self):
        self.__hit_points = None
        self.__health_points = None

    @abstractmethod
    def set_hit_points(self):
        pass

    @abstractmethod
    def set_health_points(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Hero:
    heros = ['Iron man', 'Captain America']

    power_bonus = {
        'laser': 10,
        'punches and kicks': 5,
        'strength': 8,
        'strategy': 3,
    }

    defense_bonus = {
        'armor': 5,
        'shield': 4,
        'natural armor': 4,
        'movement': 2
    }

    @staticmethod
    def get_hero():
        return random.choice(Hero.heros)

    @staticmethod
    def factory(hero_type, name):
        if hero_type == 'Iron man':
            return IronMan(name)
        elif hero_type == 'Captain America':
            return CaptainAmerica(name)
        else:
            return None

class IronMan(Character, Hero):
    def __init__(self, name):
        Character.__init__(self)
        self.type = 'Iron man'
        self.__name = name
        self.__power = 'laser'


    def set_new_special_power(self, power):
        self.__power = power

    def set_hit_points(self):
        points = random.randint(5, 10)
        self.__hit_points = points

    def set_health_points(self):
        points = random.randint(45, 60)
        self.__health_points = points

    def get_info(self):
        print('####### INFO ####### INFO')
        print(f'Hero: {self.type}')
        print(f'Special power: {self.__power}')
        print(f'Hit points: {self.__hit_points}')
        print(f'Health points: {self.__health_points}')

class CaptainAmerica(Character, Hero):
    def __init__(self, name):
        Character.__init__(self)
        self.type = 'Captain america'
        self.__name = name
        self.__power = 'strategy'


    def set_new_special_power(self, power):
        self.__power = power

    def set_hit_points(self):
        points = random.randint(5, 10)
        self.__hit_points = points

    def set_health_points(self):
        points = random.randint(45, 60)
        self.__health_points = points

    def get_info(self):
        print('####### INFO ####### INFO')
        print(f'Hero: {self.type}')
        print(f'Special power: {self.__power}')
        print(f'Hit points: {self.__hit_points}')
        print(f'Health points: {self.__health_points}')


hero = Hero.get_hero()
her_obj = Hero.factory(hero, 'Luke')
her_obj.set_hit_points()
her_obj.set_health_points()
her_obj.get_info()