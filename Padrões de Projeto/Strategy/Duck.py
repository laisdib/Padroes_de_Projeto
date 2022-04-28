'''Duck decidirá seu comportamento de vôo em vez de usar
métodos fly definidos na classe/subclasse Duck.'''

from abc import ABC, abstractmethod

class Flyable(ABC):
    # Informa que há muitas funções redundantes
    @abstractmethod
    def fly(self):
        pass


class Duck(ABC):
    def __init__(self):
        self.flyable: Flyable = None

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def quack(self):
        pass

    def performFly(self):
        return self.flyable.fly()

    def setFlyBehaviour(self, fly_behaviour: Flyable):
        self.flyable = fly_behaviour


class FlyWithWings(Flyable):
    def fly(self):
        return "fly with wings"


class FlyWithRockets(Flyable):
    def fly(self):
        return "fly with rockets"


class RedheadDuck(Duck):
    def __init__(self):
        super().__init__()
        self.flyable = FlyWithWings()

    def swim(self):
        return "paddling"

    def quack(self):
        return "basic quack"

    def display(self):
        return "redhead duck"


# Os objetos podem reutilizar o método fly
class BlueheadDuck(Duck):
    def __init__(self):
        super(BlueheadDuck, self).__init__()
        self.flyable = FlyWithRockets()

    def swim(self):
        return "paddling"

    def quack(self):
        return "basic quack"

    def display(self):
        return "blue head duck"


if __name__ == '__main__':
    redhead_duck = RedheadDuck()
    bluehead_duck = BlueheadDuck()

    print(redhead_duck.performFly())
    print(bluehead_duck.performFly())