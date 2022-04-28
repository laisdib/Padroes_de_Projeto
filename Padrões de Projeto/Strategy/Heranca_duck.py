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

    def fly(self):
        return "fly with wings"


class RedheadDuck(Duck):

    def swim(self):
        return "paddling"

    def quack(self):
        return "redhead quack"

    def display(self):
        return "redhead duck"


# Pato de borracha não deveria conseguir voar
class RubberDuck(Duck):
    
    def display(self):
        return "rubber duck"

    def swim(self):
        return "floating"

    def quack(self):
        return "jioooo"

    def fly(self):
        # Substituindo para o pato de borracha não voar
        return "I can't fly"


def let_the_duck_fly(duck: Duck) -> None:
    print(f"{duck.display()} flies: {duck.fly()}")


if __name__ == '__main__':
    rubber_duck = RubberDuck()
    redhead_duck = RedheadDuck()

    let_the_duck_fly(redhead_duck)
    # confusing to have a fly method
    let_the_duck_fly(rubber_duck)