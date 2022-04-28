from abc import ABC, abstractmethod

class Duck(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def quack(self):
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class RedheadDuck(Duck, Flyable):

    def swim(self):
        return "paddling"

    def quack(self):
        return "basic quack"

    def fly(self):
        return "fly with wings"

    def display(self):
        return "redhead duck"


# Pato de cabeça azul voa assim como o de cabeça vermelha
# Muitos outros patos como esses precisam do método fly
class BlueheadDuck(Duck, Flyable):

    def swim(self):
        return "paddling"

    def quack(self):
        return "basic quack"

    def fly(self):
        return "fly with wings"

    def display(self):
        return "blue head duck"


# Pato de borracha não deveria conseguir voar
class RubberDuck(Duck):

    def display(self):
        return "rubber duck"

    def swim(self):
        return "floating"

    def quack(self):
        return "jioooo"


if __name__ == '__main__':
    rubber_duck = RubberDuck()
    redhead_duck = RedheadDuck()