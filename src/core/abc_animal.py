from abc import ABC, abstractmethod
from dataclasses import dataclass

__all__ = ["IAnimal"]


@dataclass
class AnimalData:
    name: str
    energy: int = 100


class IAnimal(ABC, AnimalData):


    def say(self):
        print(f"Hello, i'm {self.__class__.__name__} and my name is {self.name}")

    def get_energy(self) -> int:
        return self.energy

    @abstractmethod
    def run(self):
        ...

    @abstractmethod
    def swim(self):
        ...

    @abstractmethod
    def fly(self):
        ...
