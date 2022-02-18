import numpy as np


class Product:
    """Creating a generate product wrapper class with generic attributes and a random product identifier"""

    def __init__(
        self,
        name,
        price=10,
        weight=20,
        flammability=0.5,
        identifier=np.random.randint(
            1000000,
            9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """A simple function that displays how stealable a product is based on it's price/weight ratio"""
        ratio = self.price / self.weight
        if ratio < 0.5:
            return"Not so stealable..."
        elif ratio < 1:
            return"Kinda stealable."
        else:
            return"Very stealable!"

    def explode(self):
        ratio = self.flammability * self.weight
        if ratio < 10:
            return'...fizzle.'
        elif ratio < 50:
            return'...boom!'
        else:
            return'...BABOOM!!'


class BoxingGlove(Product):
    def __init__(
        self,
        name,
        price=10,
        weight=10,
        flammability=0.5,
        identifier=np.random.randint(
            1000000,
            9999999)):
        super(
            BoxingGlove,
            self).__init__(
            name,
            price,
            weight,
            flammability,
            identifier)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
